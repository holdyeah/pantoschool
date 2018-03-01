# pantoschool
this is old pantochool
Tenda Academic system, username:studentID , initial password: 8888;
so i know the user number student id can enter the tenda system
# load main
google inurl:pantoschool find have http://*****/pantoschool/xt/accounts/login2.aspx?returnurl=%2fpantoschool
# __EVENTVALIDATION and __VIEWSTATE
__EVENTVALIDATION:

__EVENTVALIDATION is only used to verify whether the event is sent from the legitimate page,
just a digital signature, it is generally very short.
Hidden fields with "id" attribute "__EVENTVALIDATION" are new security measures for ASP.NET 2.0.
This feature can block unauthorized requests sent from the browser side by potentially malicious users.
To ensure that each postback and callback event comes from the expected user interface element,
the ASP.NET runtime adds an additional validation layer to the event.
The server side submits the content of the request by examining the form,
matching it with the information in the "__EVENTVALIDATION" hidden field with the "id" attribute.
According to the matching result, it is verified that no additional input fields
(possibly maliciously added by the user on the browser side) are added to the browser end,
and the value is selected from a list known by the server. The ASP.NET runtime will create event
validation fields during the build, and this is the moment when the information is most unlikely to be obtained.
Like view state, the event validation field contains a hash value to prevent browser-side tampering.
Description: "id" attribute "__EVENTVALIDATION" hidden fields are generally at the bottom of the form,
if the form has not been parsed in the browser side, the user submitting data may result in validation failure.

__VIEWSTATE
ViewState is a mechanism used to save the state value of a WEB control when it is returned in ASP.NET.
In the WEB FORM (FORM) is set to runat = "server", this form (FORM) will be attached to a hidden attribute _VIEWSTATE.
_VIEWSTATE stores the state values of all controls in ViewState.
ViewState is a class in Control, and all other controls get ViewState by inheriting Control.
Its type is system.Web.UI.StateBag, a collection of name / value objects.
When a page is requested, ASP.NET serializes the state of all controls into a string and sends it to the client as a hidden property of the form.
When the client returns the page, ASP.NET parses the return form attribute and assigns the value to the control

construct a payload field:
payload = {
        '__EVENTVALIDATION': '',
        '__VIEWSTATE':'',
        '__VIEWSTATEGENERATOR': 'B1CEE7C8',
        'txtUserName': '',
        'txtUserPwd': '',
        'rdoSelect': '',
        'btnLogin.x': '',
        'btnLogin.y': '',
        }

Get __EVENTVALIDATION and __VIEWSTATE values with BeautifulSoup this library
soup=BeautifulSoup(index.content,'lxml')
value1=soup.find('input',id='__VIEWSTATE')['value']
value2=soup.find('input',id='__EVENTVALIDATION')['value']


# Environmental configuration
python 2.7