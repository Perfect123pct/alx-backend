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

const setNewSchool = (schoolName, value, callback) => {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      callback(err);
    } else {
      callback(null, reply);
    }
  });
};

const getAsync = async (schoolName) => {
  return new Promise((resolve, reject) => {
    client.get(schoolName, (err, value) => {
      if (err) {
        reject(err);
      } else {
        resolve(value);
      }
    });
  });
};

const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.log(err);
  }
};

displaySchoolValue('Holberton');

setNewSchool('HolbertonSanFrancisco', '100', (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log(reply);
  }
});

displaySchoolValue('HolbertonSanFrancisco');

