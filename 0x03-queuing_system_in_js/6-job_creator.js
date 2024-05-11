import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, World!',
};

const job = queue.createJob('push_notification_code', jobData)
  .removeOnComplete(true)
  .save((err) => {
    if (err) {
      console.log('Notification job failed');
    } else {
      console.log(`Notification job created: ${(link unavailable)}`);
    }
  });

queue.on('job complete', (id) => {
  console.log('Notification job completed');
});

queue.on('job failed', (id) => {
  console.log('Notification job failed');
});

