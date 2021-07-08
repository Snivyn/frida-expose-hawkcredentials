import frida, sys

script = '''
var hooking = ObjC.classes['HawkCredentials']['- initWithHawkId:withKey:withAlgorithm:'];

Interceptor.attach(hooking.implementation, {
	onEnter: function (args) {
		console.log("Found HawkId: " + new ObjC.Object(args[2]).toString());
		console.log("Found Key: " + new ObjC.Object(args[3]).toString());
	},
});
'''
bundle = input("Please specify app bundle: ").strip()


# Connect to USB device
device = frida.get_usb_device(1000)

# Launch app and store PID
pid = device.spawn([bundle])

# Inject script
device.attach(pid).create_script(script).load()
device.resume(pid)
sys.stdin.read()
