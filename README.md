# coding_challenge
# Usage

Each solution can be imported as poker_hand_problem and fib_problem. Running the main function will also print out the answer values.


# Problem

Two problems were addressed the first was a poker hand calculator. This takes in a list of 10 card hands splits in half and finds which player won each hand. This largely invovled building a label for each hand then ranking the label, comparing, and determining which hand won by relevant high cards. As a minor archeitecutre note, I probably wouldn't nomrally structure this as one module containing submodules but as a series of modules called by a main module. Encapsulation like this is good for sharing local variables quickly but leads to some issues debugging.

The next was adding every even fibonacci number under 4 million this involved building a fibonacci sequence calcaultor and adding any number that was 0 when modulo 2 to find even values.
