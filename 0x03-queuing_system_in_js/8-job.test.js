const chai = require('chai');
const expect = chai.expect;
const kue = require('kue');
const queue = kue.createQueue();
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', function () {
    before(function () {
        // Activate test mode
        queue.testMode.enter();
    });

    afterEach(function () {
        // Clear the test queue
        queue.testMode.clear();
    });

    after(function () {
        // Exit test mode
        queue.testMode.exit();
    });

    it('should throw an error if jobs is not an array', function () {
        expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, 'Jobs is not an array');
    });

    it('should create jobs for each item in the jobs array', function () {
        const jobs = [
            { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
            { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' }
        ];

        createPushNotificationsJobs(jobs, queue);

        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
    });
});
