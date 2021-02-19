import os
print([f for f in os.listdir('/home/dokaja/ed/html_css_js_tutorial') ]) if os.path.isfile(os.path.join('/home/students', f))