import os
import cgi
import urllib

import jinja2

import webapp2
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(autoescape=True, loader = jinja2.FileSystemLoader(template_dir))

#Main page class is for all items on the Home page
class MainPage(webapp2.RequestHandler):
	def get(self):
	
		template_notes={
			'title': 'Introduction to Programming',


			'subheadings':[['Unit 4 - 4.1: Introduction to Networks', 
			'''<p>A <b> network </b> is a group of entities that can communicate, even though they are not directly connected.</p> 

			<p><b>There are many types of computer networks, including the following:</b></p>  
			<ul> 
				
				<li>local-area networks (LANs): The computers are geographically close together (that is, in the same building).</li>
				<li> wide-area networks (WANs): The computers are farther apart and are connected by telephone lines or radio waves. </li>
				<li>campus-area networks (CANs): The computers are within a limited geographic area, such as a campus or military base.</li>
			</ul>	
			
			<p><img src="https://sp.yimg.com/ib/th?id=JN.%2bJN6GZ9c7fbxfm0OVrATjA&pid=15.1&P=0" style="max-width:100%;" alt="Network"> </p>

			<p><b>How to make a Network Work:</b></p>  
			<ul>
				
				<li>We need a way to encode and interpret messages</li>
				<li>We need a way to route messages</li>
				<li>We need rules!</li>		

			</ul>

			<p><b> Measuring Networks</b></p>  
			<ul> 
				
				<li> <b> Latency</b> Time it takes for a message to get from the source to the destination, from the start of the message, unit of time measured in milliseconds today </li>
				<li> <b> Bandwith</b> Amount of information that can be transmitted per unit time, once you have some part of the message across what is the rate it can be received. Can be measured in MBPS(Megs bit's per second) </li>
				<li> <b> Bit</b> 1 bit = smallest unit of information, in computing we think of it as 0 and 1, If you have more bits you can encode more things </li>
				<li> <b> Protocal</b> set of rules that people agree to that set a policy on how to get through the internetOn the web we use HTTP - Hypertext Transfer Protocol </li>
			</ul>	
			</ul>	

			'''],

			['4.2: Make the Internet Work for you', 
			'''
			<p> A  <b>HTML structure</b> An HTML 4 document is composed of three parts: </p>

			<p> <b>Breaking down a URL</b></p>

			<ul> 
				
				<li><b>http://:</b> "HTTP" stands for Hypertext Transfer (or Transport) Protocol, and is the identification technology used to communicate between Web servers and the users who access their information.</li>
				<li>  <b>domain name: </b> The domain name is the textual representation of the IP address, used to identify a specific Web page or pages, and comes after the "://".</li>
				<li><b>forward slash,then file name:</b> Path or Directory on the computer to a file </li>
				<li><b>name of file:</b> name of file, usually ending in .html or .htm.</li>
			</ul>	
			
			<p><img src="https://sp.yimg.com/ib/th?id=JN.6L3izw%2bnQUJluHPswJoi%2fA&pid=15.1&P=0" alt="HTML Structure"> </p>

			<p> <b>Get and Post</b></p>

			<ul> 
				
				<li><b> POST - Submits data to be processed to a specified resource </b> Note that query strings (name/value pairs) is sent in the HTTP message body of a POST reques. </li>
				<li> <b> GET - Requests data from a specified resource </b> Note that query strings (name/value pairs) is sent in the URL of a GET request.</li>
			
			</ul>

			<p> <b>Absolute vs. Relative Path</b></p>

			<ul> 
				
				<li>An absolute path is the full URL to a file.</li>
				<li>A relative path points to the location of the file you want to link to in relation to the page being viewed, all within your server space.</li>
			
			</ul>

			<p> <b>What is a Query Parameter </b> a parameter query is a query that prompts the user to enter specific criteria every time the query is run.</p> 
			
			<p> <b>Caching </b> A cache is something that stores data so that you don't have to retrieve it later. It can be used to make data requests faster. </p>


			<p> <b>HTTP Response Errors </b></p>

				<p><img src="https://sp.yimg.com/ib/th?id=JN.SKr%2byjOixEVzZK%2bm6bR77w&pid=15.1&P=0" alt="Response Error"> </p>

				</p>The following is a list of Hypertext Transfer Protocol (HTTP) response status codes. This includes codes from IETF internet standards as well as other IETF RFCs, other specifications and some additional commonly used codes. </p>

				<p> HTTP Response Errors<a href="http://en.wikipedia.org/wiki/List_of_HTTP_status_codes"> HTTP Response Errors </a>

				<p> <b>The Purpose of Servers</b></p>A server is a running instance of an application (software) capable of accepting requests from the client and giving responses accordingly. Servers can run on any computer including dedicated computers, which individually are also often referred to as "the server". </p>	

			'''],

			['4.3: HTML Forms', '''

			<p> <b>The Form Element</b> HTML forms are used to collect user input. The FORM element defines an HTML form. HTMl forms contain form elements. Form elements are different types of input elements, checkboxes, radio buttons, submit buttons, and more. </p>

				<p> 1) The input element is the most important, and has many variations, depending on the type attribute. (text, radio, and submit.)input type text defines a one line field or text input. </p>
				<p> 2) Submit defines a button for submitting a form to a form-handler.</p>
				<p> 3)The action attribute defines the action to be performed when the form is submitted. </p>
				<p> 4)The method attribute specifies the HTTP method (GET or POST) to be used when submitting the forms. </p>

				<p> HTML Forms <a href="http://www.w3schools.com/html/html_forms.asp"> HTML Forms </a>

				<p><img src="https://sp.yimg.com/ib/th?id=JN.ySlwcshaO8e4MkqBo6Z8qg&pid=15.1&P=0" alt="HTML Form"> </p>'''],




			['4.4: Python Break Modules and Dictionaries', '''

			<p> <b>The Modulus Operator:</b> This is an operator (like +, -, *, or /) that every programming language has.</p>

			<p> <b>Dictionaries:</b> This is another data structure, similar to a Python List. A dictionary data structure is one which is capable of storing objects in sorted order based on key such as a string or an integer. </p>
			
			<p> Dictionaries <a href="https://docs.python.org/3/tutorial/datastructures.html#dictionaries"> Dictionaries</a>
			'''],

			['4.5: Google App Engine', '''

			<p><b>Google App Engine</b> let's you build and run applications on Googles Infrastructure</p> 

			<p> App Engine includes a simple web application framework, called webapp2. The webapp2 framework is already installed in the App Engine environment and in the SDK.  </p>

			<p> Google App Engine <a href="https://cloud.google.com/appengine/docs/python/"> App Engine</a>	

				<p> App Engine includes a simple web application framework, called webapp2. The webapp2 framework is already installed in the App Engine environment and in the SDK.  </p>

				<p> A <b> webapp2 application </b> has two parts: 1) one or more RequestHandler classes that process requests and 2) build response a WSGIApplication instance that routes incoming requests to handlers based on the URL </p>

				<p> Google App Engine Python Tutorial <a href="https://cloud.google.com/appengine/docs/python/gettingstartedpython27/introduction"> Python Tutorial</a>	


			  '''],


			['4.6: Validation', '''

			<p> <b>Validation</b> Verification on the server side that we expect to see what we expected to see </p>

				<p> Data validation is the process of ensuring that computer input is clean, correct, and useful. Typical validation tasks are: 1) has the user filled in all required fields? 2) has the user entered a valid date? 3) has the user entered text in a numeric field?</p>


				<p> Most often, the purpose of data validation is to ensure correct input to a computer application. Validation can be defined by many different methods, and deployed in many different ways.</p>

				<p> <b>Server side validation </b> is performed by a web server, after input has been sent to the server.</p>


				<p> <b>Client side validation </b> is performed by a web browser, before input is sent to a web server.</p>

				<p>String Substitution</p> With String Substitution you can replace a string with the % sign. Than you can call the string with %OTHERSTRING when the OTHERSTRING can also be a variable. 

				<p><b>Escaping</b> HTML allows you to escape certain methods or change them. Correct way to include text in rendered HTML.</p>

			'''],


			  ['4.7: HTML Templates', '''

			  <p> Templates are a great way to seperate different types of code, make more readable code, more secure websites, and HTML is easy to modify.  </p>

			  <p> There is a better way using Template - a template library is a library to build complicated stings </p>

			  <p> HTML embedded in code is messy and difficult to maintain. It's better to use a templating system, where the HTML is kept in a separate file with special syntax to indicate where the data from the application appears. </p>

			<p> <b>Helpful Tips</b></p>

			<ul> 
				
				<li>Always automatically escape variables when possible.</li>
				<li>Minimize the code that you include in templates</li>
				<li>Minimize html in code (good rule is zero html in code)</li>
				<li>Use Template Inheritance: This lets you define a base template which you can later plug new HTML into. This is useful when, for example, you want to have a consistent header and footer across your app.</li>
				<li>For Loops</b>Add Repeated Elements: If you've got many divs that all have the same structure, it's much better to use a for loop.</li>
			</ul>

			  '''],


			   ['4.8 DataBase', '''

			   <p>  Databases use a series of Tables to store the data. A table simply refers to a two dimensional representation of your data using columns and rows. </p>

				<p> How does the database keep things straight? Each database table is given a unique name. Without a unique name the DBMS (DataBase Management System) would get very confused.</p>


				<p> Your table is the Primary Key. The Primary Key simply refers to a column in your table that is guaranteed unique. The Primary Key is then used for the purposes of indexing your table which makes it much more efficient to search, sort, link, etc.</p>

				<p> <b> Datastore</b> Storing data in a scalable web application can be tricky. All web servers need to be interacting with data that is also spread out across dozens of machines, possibly in different locations around the world.</p>

				<p> App Engine's data repository, the High Replication Datastore (HRD), uses the Paxos algorithm to replicate data across multiple datacenters. </p>

				<p>Data is written to the Datastore in objects known as entities. Each entity has a key that uniquely identifies it. An entity can optionally designate another entity as its parent; the first entity is a child of the parent entity.</p>

				<p> An entity's parent, parent's parent, and so on recursively, are its ancestors; its children, children's children, and so on, are its descendants. An entity without a parent is a root entity. </p>

	

				<p>Every Datastore query computes its results using one or more indexes, tables containing entities in a sequence specified by the index's properties and, optionally, the entity's ancestors.  </p>

				<p><b>An index </b> is defined on a list of properties of a given entity kind, with a corresponding order (ascending or descending) for each property. For use with ancestor queries, the index may also optionally include an entity's ancestors. </p>

			    <p><b>String substitution </b> is where we use the "%"" &"s" together to
			    substitute strings.  It's a place holder for whatever value we are plugging into that spot.  You can sub in one word, or multiple different
			    words, or even a dictionary.</p> 

			    <p>We can use string substitution to save a users input.  For instance, instead of using input type="text" value="cool", we can use "%"+(month)+"s".</p> 

			    <p><b>ACID - Atomicity, Consistency, Isolation, Durability</b></p>

				<p><b>A</b> All parts of a transaction succeed or fail together </p>

				<p><b>C</b> The database will always be consistent  </p>

				<p><b>I</b> No transaction can interfere with another's  </p>

				<p><b>D</b> Once the transaction is committed it won't be lost   </p>


			''']]
				}


		template=jinja_env.get_template('notepage.html',)

		self.response.out.write(template.render(template_notes))#this will render the html page and template values


class summaryHandler(webapp2.RequestHandler):
	def get(self):
		template_notes={
			'title': 'Introduction to Programming',
				}
		
				
		template=jinja_env.get_template('summary.html',)

		self.response.out.write(template.render(template_notes))

# Handler code sets up for the jinja template and form/guestbook integration
class myHandler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.write(*a, **kw)

	def render_str(self, template, **params):
		template = jinja_env.get_template(template)
		return template.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template,**kw))


#This code identifies the name of the wall
DEFAULT_WALL='Public'
def wall_key(wall_name=DEFAULT_WALL):
	return ndb.Key('Wall', wall_name)

#This Post class sets up the model for my datastore
class Post(ndb.Model):
	guest_name=ndb.StringProperty(indexed=False)	
	guest_message=ndb.StringProperty(indexed=False)
	date=ndb.DateTimeProperty(auto_now_add=True)

class guestbookHandler(myHandler):
	def get(self):
		wall_name = self.request.get('wall_name',DEFAULT_WALL)
		if wall_name == DEFAULT_WALL.lower(): wall_name = DEFAULT_WALL
		guest_name=self.request.get_all("guest_name")
		guest_message=self.request.get_all("guest_message")
		posts_query = Post.query(ancestor = wall_key(wall_name)).order(-Post.date)
		posts=posts_query.fetch(50)

		template_values={
		'title': 'Comment Page',
		'posts': posts,}

		template=jinja_env.get_template('guestbook.html')
		self.response.out.write(template.render(template_values))

	def post(self):
		wall_name = self.request.get('wall_name',DEFAULT_WALL)
		post = Post(parent=wall_key(wall_name))

		guest_name = self.request.get('guest_name')
		guest_message = self.request.get('guest_message')
		#error_message = self.request.get('Error name field blank')

		if type(guest_name) != unicode:
			post.guest_name != unicode(self.request.get('guest_name'))
		#if type(guest_name) != "":
	    #post.guest_name != unicode(self.request.get('error_message'))
		

		else:
			
			post.guest_name = self.request.get('guest_name')
		

		if type(guest_message) != unicode:
			post.guest_message = unicode(self.request.get('guest_message'),'utf-8')
		else:
			post.guest_message = self.request.get('guest_message')

	

		post.put()#writes to the datastore
		query_params = {'wall_name': wall_name}
		self.redirect('/guestbook.html?' + urllib.urlencode(query_params))


application=webapp2.WSGIApplication([('/', MainPage),
	('/summary.html', summaryHandler),
	('/guestbook.html', guestbookHandler)
	], 
	debug=True)
