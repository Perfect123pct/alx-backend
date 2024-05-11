import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];

const queue = kue.createQueue({
  prefix: 'push_notification_code_2',
  concurrency: 2,
});

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);
  if (blacklistedNumbers.includes(phoneNumber)) {
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    done(error);
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
};

queue.process('push_notification_code_2', sendNotification);

