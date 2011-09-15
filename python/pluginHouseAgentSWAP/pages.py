#########################################################################
#
# swap
#
# Copyright (c) 2011 Daniel Berenguer <dberenguer@usapiens.com>
#
# This file is part of the panStamp project.
#
# panStamp  is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# panStamp is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with panLoader; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301
# USA
#
#########################################################################
__author__="Daniel Berenguer"
__date__  ="$Sep 9, 2011 9:27:16 AM$"
#########################################################################

from mako.lookup import TemplateLookup
from mako.template import Template
from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET
from twisted.internet import defer


def init_pages(web, coordinator, db):
    """
    Entry point for each of the web pages
    """
    web.putChild("swap_add", SWAP_add(coordinator, db))
    web.putChild("swap_network", SWAP_network(coordinator, db))
    web.putChild("swap_added", SWAP_added(coordinator, db))


class SWAP_add(Resource):
    """
    Class that shows an add form to add a SWAP device to the HouseAgent database.
    """
    def __init__(self, coordinator, db):
        Resource.__init__(self)
        self.coordinator = coordinator
        self.db = db
        
    def result(self, result):
        
        lookup = TemplateLookup(directories=['houseagent/templates/'])
        template = Template(filename='houseagent/plugins/swap/templates/add.html', lookup=lookup)
        
        self.request.write(str(template.render(result=result[1], locations=result[0], mote=self.mote, product=self.product, pluginid=self.pluginid, pluginguid=self.pluginguid)))
        self.request.finish()
    
    def render_GET(self, request):
        
        self.request = request    
        self.mote = request.args["mote"][0]
        self.product = request.args["product"][0]
        self.pluginguid = request.args["pluginguid"][0]
        self.pluginid = request.args["pluginid"][0]
      
        deferlist = []
        deferlist.append(self.db.query_locations())
        deferlist.append(self.coordinator.send_custom(self.pluginguid, "get_motevalues", {'mote': self.mote}))
        d = defer.gatherResults(deferlist)
        d.addCallback(self.result)
        
        return NOT_DONE_YET
    
    
class SWAP_network(Resource):
    """
    Class that displays SWAP network information.
    """
    def __init__(self, coordinator, db):
        Resource.__init__(self)
        self.coordinator = coordinator
        self.db = db

    def result(self, result):
        print "result=", result
        lookup = TemplateLookup(directories=['houseagent/templates/'])
        template = Template(filename='houseagent/plugins/swap/templates/network.html', lookup=lookup)
        
        self.request.write(str(template.render(result=result, pluginguid=self.pluginguid, pluginid=self.pluginid)))
        self.request.finish()

    def query_error(self, error):
        print "FAIL:", error
    
    def render_GET(self, request):
        self.request = request
        plugins = self.coordinator.get_plugins_by_type("SWAP")
        
        if len(plugins) == 0:
            self.request.write(str("No online SWAP plugins found..."))
            self.request.finish()
        elif len(plugins) == 1:
            self.pluginguid = plugins[0].guid
            self.pluginid = plugins[0].id
            self.coordinator.send_custom(plugins[0].guid, "get_networkinfo", {}).addCallback(self.result)   
                
        return NOT_DONE_YET


class SWAP_added(Resource):
    """
    Class that adds a SWAP device to the HouseAgent database.
    """
    def __init__(self, coordinator, db):
        Resource.__init__(self)
        self.coordinator = coordinator      
        self.db = db
        
    def device_added(self, result):
        print "SWAP DEVICE ADDED! YAY!"
        
        self.request.write(str("done!")) 
        self.request.finish()             
    
    def render_POST(self, request):
        self.request = request
        data = json.loads(request.content.read())

        self.db.add_device(data['name'], data['nodeid'], data['pluginid'], data['location']).addCallback(self.device_added)
        self.coordinator.send_custom(data['pluginguid'], "track_values", {'values': data['valueids']})
        
        return NOT_DONE_YET