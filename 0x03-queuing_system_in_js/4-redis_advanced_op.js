import redis from 'redis';

const client = redis.createClient({
  host: '127.0.0.1',
  port: 6379,
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.hset('HolbertonSchools', 'Portland', 50, (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log('Reply:', reply);
  }
});

client.hset('HolbertonSchools', 'Seattle', 80, (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log('Reply:', reply);
  }
});

client.hset('HolbertonSchools', 'New York', 20, (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log('Reply:', reply);
  }
});

client.hset('HolbertonSchools', 'Bogota', 20, (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log('Reply:', reply);
  }
});

client.hset('HolbertonSchools', 'Cali', 40, (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log('Reply:', reply);
  }
});

client.hset('HolbertonSchools', 'Paris', 2, (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log('Reply:', reply);
  }
});

client.hgetall('HolbertonSchools', (err, obj) => {
  if (err) {
    console.log(err);
  } else {
    console.log(obj);
  }
});

