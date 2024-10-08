#!/usr/bin/env node

import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('should create jobs when jobs is an array', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
  });

  it('should log correct messages on job events', (done) => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      }
    ];

    const originalLog = console.log;
    const logs = [];
    console.log = (message) => logs.push(message);

    createPushNotificationsJobs(jobs, queue);

    const job = queue.testMode.jobs[0];
    job.id = 1;  // Assign an ID manually for test purposes
    job._events.complete();
    job._events.failed('Error message');
    job._events.progress(50);

    expect(logs).to.include(`Notification job created: ${job.id}`);
    expect(logs).to.include(`Notification job ${job.id} completed`);
    expect(logs).to.include(`Notification job ${job.id} failed: Error message`);
    expect(logs).to.include(`Notification job ${job.id} 50% complete`);

    console.log = originalLog;

    done();
  });
});
