const express = require('express');
const kue = require('kue');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const port = 1245;

// Create Redis client
const client = redis.createClient();

// Promisify Redis methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Kue queue
const queue = kue.createQueue();

// Seat management
let reservationEnabled = true;

async function reserveSeat(number) {
    await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
    const seats = await getAsync('available_seats');
    return parseInt(seats, 10);
}

// Initialize available seats
reserveSeat(50);

// Routes
app.get('/available_seats', async (req, res) => {
    const numberOfAvailableSeats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
    if (!reservationEnabled) {
        return res.json({ status: 'Reservation are blocked' });
    }

    const job = queue.create('reserve_seat').save(err => {
        if (!err) {
            return res.json({ status: 'Reservation in process' });
        }
        return res.json({ status: 'Reservation failed' });
    });

    job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
    });

    job.on('failed', (err) => {
        console.log(`Seat reservation job ${job.id} failed: ${err}`);
    });
});

app.get('/process', (req, res) => {
    res.json({ status: 'Queue processing' });

    queue.process('reserve_seat', async (job, done) => {
        const currentSeats = await getCurrentAvailableSeats();

        if (currentSeats > 0) {
            await reserveSeat(currentSeats - 1);
            if (currentSeats - 1 === 0) {
                reservationEnabled = false;
            }
            done();
        } else {
            done(new Error('Not enough seats available'));
        }
    });
});

// Start server
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
