import kue from 'kue';

const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  jobs.forEach((job) => {
    const notificationJob = queue.createJob('push_notification_code_3', job)
      .removeOnComplete(true)
      .save((err) => {
        if (err) {
          console.log(`Notification job failed: ${err.message}`);
        } else {
          console.log(`Notification job created: ${(link unavailable)}`);
        }
      });
    notificationJob.on('complete', () => {
      console.log(`Notification job ${(link unavailable)} completed`);
    });
    notificationJob.on('failed', (err) => {
      console.log(`Notification job ${(link unavailable)} failed: ${err.message}`);
    });
    notificationJob.on('progress', (progress) => {
      console.log(`Notification job ${(link unavailable)} ${progress}% complete`);
    });
  });
};

export default createPushNotificationsJobs;

