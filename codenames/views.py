from django.http import HttpResponse

# Create your views here.
def index_page(request):
	# TODO:// implement templates
	output = '''
	    <html>
	      <head><title>%s</title></head>
	      <body>
	        <h1>%s</h1><p>%s</p>
	      </body>
	    </html>
	  ''' % (
	    'NICKA Index',
	    'NICKA is Under Construction',
	    'This website is currently under construction. Please try again later.'
  )

	return HttpResponse(output)

def op_detail_page(request, operation_id):
	# TODO:// implement view page by op code
	return HttpResponse("Op #%s" % operation_id)