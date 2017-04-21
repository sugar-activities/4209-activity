#!/usr/bin/python
try:
	from sugar.activity import bundlebuilder
	bundlebuilder.start()
except ImportError:
	import os
	os.system("find ./ | sed 's,^./,HelloWorldActivity.activity/,g' > MANIFEST")
	os.system('rm HelloWorldActivity.xo')
	os.chdir('..')
	os.system('zip -r HelloWorldActivity.xo HelloWorldActivity.activity')
	os.system('mv HelloWorldActivity.xo ./HelloWorldActivity.activity')
	os.chdir('HelloWorldActivity.activity')

