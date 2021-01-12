LED_OFF();
                                                   
ros.on('connection', function() {console.log('websocket: connected');});
ros.on('error', function(error) {console.log('websocket error: ', error); });
ros.on('close', function() {console.log('websocket: closed');});

function LED_ON(){
	console.log("ON");
	let name = '/ledon';
	console.log(name)
	let ros=new ROSLIB.Ros({url:'ws://'+location.hostname+':9090'});
	
	let ledon = new ROSLIB.Topic({
		ros:ros,
		name:name,
		messageType:'std_msgs/Int8'
	});
	let data = new ROSLIB.Message({data:1});
	ledon.publish(data);
}

function LED_OFF(){
	console.log("OFF");
	let name = '/ledoff';
	console.log(name)
	let ros=new ROSLIB.Ros({url:'ws://'+location.hostname+':9090'});
	let ledoff = new ROSLIB.Topic({
		ros:ros,
		name:name,
		messageType:'std_msgs/Int8'
	});
	let data = new ROSLIB.Message({data:0});
	ledoff.publish(data);
}
