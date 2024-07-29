import kue from 'kue';

const queue = kue.createQueue();

const data = {
	phoneNumber: '0123456789',
	message: 'job message'
};
const job = queue.create('push_notification_code', data)
	.save((err) => {
		if (err) {
			console.log('error creating job');
		}
		else {
			console.log(`Notification job created: ${job.id}`);
		}
	});

job.on('complete', () => {
	console.log('Notification job completed');
});
job.on('failed', () => {
	console.log('Notification job failed');
});
