#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import jinja2
import os

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

import cgi
import datetime
import urllib
import webapp2

from xml.dom.minidom import parse, parseString

class MainPage(webapp2.RequestHandler):
    def get(self):
	jobs = []
        sourceUrl = 'https://gs10.globalsuccessor.com/GuardianNewsHotJobs/'
        dom= parse(urllib.urlopen(sourceUrl))

        hotJobs=dom.getElementsByTagName('HotJobs')

        for node in hotJobs:
            jobslist=node.getElementsByTagName('HotJob')
    	    for job in jobslist:
                jobTitle = job.getElementsByTagName("PositionTitle")[0].childNodes[0].nodeValue
                jobLink = job.getElementsByTagName("JobDescriptionURL")[0].childNodes[0].nodeValue
 
		jobs.append((jobTitle,jobLink))			

            template_values = {
               'jobs': jobs
                }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage)],debug=True)


