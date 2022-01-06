///usr/bin/env jbang "$0" "$@" ; exit $?
//DEPS org.assertj:assertj-core:3.21.0

package ch06.jbang.dailyepsilon;

import java.util.stream.Collectors;
import java.util.stream.IntStream;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.within;

public class Problem20220106 {

    public static void main(String[] args) {

        var iterations = 10_0000_000;

        //Sum(1/x^2)=Pi^2/6
        var op1 = IntStream.rangeClosed(1, iterations).boxed()
            .map(n -> 1 / Math.pow(n, 2))
            .collect(Collectors.summingDouble(Double::doubleValue));
        var op2 = (Math.PI * Math.PI) / 6;

        System.out.println(op1);
        System.out.println(op2);
        
        assertThat(op1).isCloseTo(op2, within(Double.valueOf("1E-8")));
    }
}

