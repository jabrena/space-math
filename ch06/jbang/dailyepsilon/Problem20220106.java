///usr/bin/env jbang "$0" "$@" ; exit $?
//DEPS org.assertj:assertj-core:3.21.0

package ch06.jbang.dailyepsilon;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.stream.IntStream;

public class Problem20220106 {

    public static void main(String[] args) {

        var iterations = 100000;
        var roundingMode = RoundingMode.HALF_UP;

        var op1 = BigDecimal.valueOf(Math.PI).pow(2);
        var op2 = IntStream.rangeClosed(1, iterations).boxed()
            .map(BigDecimal::valueOf)
            .map(n -> BigDecimal.ONE.divide(n.pow(2), roundingMode))
            .reduce(BigDecimal.ZERO, BigDecimal::add);

        var result = op1.divide(op2, roundingMode);

        System.out.println(op2);
    }
}

