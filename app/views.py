from app import app
from flask import  render_template,url_for
import requests

@app.route('/login', methods=['POST', 'GET'])
def login():
    pass
    return render_template ('login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    pass
    return render_template ('signup.html')

# NEW DISPLAY PAGES
#..................................................................................#

@app.route('/')
def indexPg():
   return render_template ('index2.html', data = get_governors())

def get_governors():
    auth_token = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJuYW1laWQiOiJqb2hud2Fob21lIiwibmJmIjoxNjEyMjU0NDQ2LCJleHAiOjE2MTI4NTkyNDYsImlhdCI6MTYxMjI1NDQ0Nn0.sLNJCDdIhiKA8O_bLaOgAQYp-cPpdQKzBFy9KqgWuINxLqb2k7q2hfjmyxaRUXaDtZ9RQZio-K_tklXDnWwgUA'
    hed = {'Authorization': 'Bearer ' + auth_token}

    url = 'http://41.89.227.168:5022/api/SpeedGovernor/1'
    response = requests.get(url, headers=hed)
    data = response.json()
    data_list = list(data.items())
   # list_from_string = json.loads(response)
    print(data_list)
    print(data)
    return data 

@app.route('/typography')
def typography():
   pass
   return render_template ('pages/typography.html')

@app.route('/terrain')
def terrain():
   pass
   return render_template ('terrain.html')



@app.route('/infobox5')
def infobox5():
   pass
   return render_template ('pages/widgets/infobox/infobox-5.html')

@app.route('/alerts')
def alerts():
   pass
   return render_template ('pages/ui/alerts.html')

@app.route('/animations')
def animations():
   pass
   return render_template ('pages/ui/animations.html')

@app.route('/badges')
def badges():
   pass
   return render_template ('pages/ui/badges.html')


@app.route('/breadcrumbs')
def breadcrumbs():
   pass
   return render_template ('pages/ui/breadcrumbs.html')

@app.route('/buttons')
def buttons():
   pass
   return render_template ('pages/ui/buttons.html')

@app.route('/collapse')
def collapse():
   pass
   return render_template ('pages/ui/collapse.html')

@app.route('/colors')
def colors():
   pass
   return render_template ('pages/ui/colors.html')

@app.route('/dialogs')
def dialogs():
   pass
   return render_template ('pages/ui/dialogs.html')


@app.route('/icons')
def icons():
   pass
   return render_template ('pages/ui/icons.html')

@app.route('/labels')
def labels():
   pass
   return render_template ('pages/ui/labels.html')


@app.route('/list_group')
def list_group():
   pass
   return render_template ('pages/ui/list-group.html')


@app.route('/media_object')
def media_object():
   pass
   return render_template ('pages/ui/media-object.html')


@app.route('/modals')
def modals():
   pass
   return render_template ('pages/ui/modals.html')


@app.route('/notifications')
def notifications():
   pass
   return render_template ('pages/ui/notifications.html')

@app.route('/pagination')
def pagination():
   pass
   return render_template ('pages/ui/pagination.html')

@app.route('/preloaders')
def preloaders():
   pass
   return render_template ('pages/ui/preloaders.html')

@app.route('/progressbars')
def progressbars():
   pass
   return render_template ('pages/ui/progressbars.html')

@app.route('/range_sliders')
def range_sliders():
   pass
   return render_template ('pages/ui/range-sliders.html')


@app.route('/sortable_nestable')
def sortable_nestable():
   pass
   return render_template ('pages/ui/sortable-nestable.html')



@app.route('/tabs')
def tabs():
   pass
   return render_template ('pages/ui/tabs.html')



@app.route('/thumbnails')
def thumbnails():
   pass
   return render_template ('pages/ui/thumbnails.html')


@app.route('/tooltips_popovers')
def tooltips_popovers():
   pass
   return render_template ('pages/ui/tooltips-popovers.html')



@app.route('/waves')
def waves():
   pass
   return render_template ('pages/ui/waves.html')



@app.route('/basic_form_elements')
def basic_form_elements():
   pass
   return render_template ('pages/forms/basic-form-elements.html')

@app.route('/advanced_form_elements')
def advanced_form_elements():
   pass
   return render_template ('pages/forms/advanced-form-elements.html')


@app.route('/form_examples')
def form_examples():
   pass
   return render_template ('pages/forms/form-examples.html')


@app.route('/form_validation')
def form_validation():
   pass
   return render_template ('pages/forms/form-validation.html')


@app.route('/form_wizard')
def form_wizard():
   pass
   return render_template ('pages/forms/form-wizard.html')



@app.route('/editors')
def editors():
   pass
   return render_template ('pages/forms/editors.html')




@app.route('/normal_tables')
def normal_tables():
   pass
   return render_template ('pages/tables/normal-tables.html')



@app.route('/jquery_datatable')
def jquery_datatable():
   pass
   return render_template ('pages/tables/jquery-datatable.html')



@app.route('/editable_table')
def editable_table():
   pass
   return render_template ('pages/tables/editable-table.html')

@app.route('/morris')
def morris():
   pass
   return render_template ('pages/charts/morris.html')




@app.route('/flot')
def flot():
   pass
   return render_template ('pages/charts/flot.html')




@app.route('/chartjs')
def chartjs():
   pass
   return render_template ('pages/charts/chartjs.html')




@app.route('/sparkline')
def sparkline():
   pass
   return render_template ('pages/charts/sparkline.html')



@app.route('/jquery_knob')
def jquery_knob():
   pass
   return render_template ('pages/charts/jquery-knob.html')


@app.route('/profile')
def profile():
   pass
   return render_template ('pages/examples/profile.html')


@app.route('/forgot_password')
def forgot_password():
   pass
   return render_template ('pages/examples/forgot-password.html')



@app.route('/blank')
def blank():
   pass
   return render_template ('pages/examples/blank.html')



@app.route('/404')
def error404():
   pass
   return render_template ('pages/examples/404.html')




@app.route('/500')
def error500():
   pass
   return render_template ('pages/examples/500.html')



@app.route('/google')
def google():
   pass
   return render_template ('pages/maps/google.html')

@app.route('/changelogs')
def changelogs():
   pass
   return render_template ('pages/changelogs.html')



# @app.route('/google')
# def google():
#    pass
#    return render_template ('')



