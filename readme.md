# Readme

If we assume that (a) the hash rate is constant the whole time, a new block will be mined once every 10 minutes on average (from whitepaper), (b) mining events are independent of each other, (c) Two blocks cannot be mined at the same time
then we can model it as a Homogeneous Poisson Process with an average rate lambda=6 (blocks/hr)

Let us denote T_n as the elapsed time between the (n-1)st and the nth mining event, since the events follow a Poisson Process, T_n, n=1,2,3... are independent identically distributed exponential random variables having mean 1/lambda. (Refer to Introduction to Probability Models, Proposition 5.1).
Now, let us calculate the probability that the elapsed time between two blocks exceeds 2 hours:


P(T_n > 2) = e^(-lambda\*2) = e^(-6*2) = 6.1442123533 * 10^-6

Let X be a random variable denoting the number of blocks mined until the elapsed time between the last two blocks is greater than two hours, then X follows a geometric distribution:


P(X=k) = (1-p)^(k-1) * p where p = P(T_n > 2)

The expected number of blocks till we see such event is 


E[X] = 1/p = 1/(6.1442123533 * 10^-6) = 162754.79141975117255 blocks

And the expected waiting time till we see such event is


E[T_n] * E[X] = 1/lambda * 403.42879 = 1/6 (hr/block) * 162754.79141975117255 (# of blocks) = 27125 hr

In summary, we are expecting to see two consecutive blocks mined more than 2 hours apart after 162754.79141975117255 blocks or 27125 hr.
The latest block is 752087, which implies there are 752087/162754.79141975117255 = 4.62 such events occurred in the past on average


However, based our script, there are 142 such events.

A possible reason for this is that the hash rate is generally
increasing over time, and the method by which the difficulty
is updated means that the difficulty lags behind the hash rate
by about two weeks. Consequently, the average rate at which
blocks are mined is greater than six blocks per hour due to the
delay in adjusting the difficulty. Furthermore, the hash rate and
hence the block arrival rate usually increases over the course
of a segment until the end of the segment when the difficulty
is increased to compensate, and the arrival rate is reduced. 
(reference [Block arrivals in the Bitcoin blockchain](https://arxiv.org/pdf/1801.07447.pdf))

Other possible reasons:

* We are not considering propagation delay between nodes.
* Nonhomogeneous poisson process where hash rate is periodic is more appropriate model for this. (reference [Block arrivals in the Bitcoin blockchain](https://arxiv.org/pdf/1801.07447.pdf))


