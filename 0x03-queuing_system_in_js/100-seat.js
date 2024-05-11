import express from 'express';
import Redis from 'redis';
import kue from 'kue';

const app = express();
const client = Redis.createClient();
const queue = kue.createQueue();

let availableSeats = 50;
let reservationEnabled = true;

const reserveSeat = async (number) => {
  await client.set('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const seats = await client.get('available_seats');
  return parseInt(seats) || 0;
};

app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }
  const job = queue.createJob('reserve_seat', {}).save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });
  job.on('complete', () => {
    console.log(`Seat reservation job ${(link unavailable)} completed`);
  });
  job.on('failed', (err) => {
    console.log(`Seat reservation job ${(link unavailable)} failed: ${err.message}`);
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });
  queue.process('reserve_seat', async (job, done) => {
    const seats = await getCurrentAvailableSeats();
    if (seats <= 0) {
      return done(new Error('Not enough seats available'));
    }
    await reserveSeat(seats - 1);
    if (seats - 1 === 0) {
      reservationEnabled = false;
    }
    done();
  });
});

app.listen(1245, () => {
  console.log('Server listening on port 1245');
  reserveSeat(50);
});

