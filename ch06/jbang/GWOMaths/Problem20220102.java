///usr/bin/env jbang "$0" "$@" ; exit $?
//DEPS org.assertj:assertj-core:3.21.0

package ch06.jbang.GWOMaths;

import java.math.MathContext;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.function.Predicate;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.within;

public class Problem20220102 {

    public static void main(String[] args) {

        var iterations = 1000;
        Predicate<Integer> isPerfect = n -> {
            var sum = IntStream.range(1, n - 1)
                .filter(i -> (n % i == 0) ? true : false)
                .reduce(0, Integer::sum);
            return (sum == n) ? true : false;
        };

        var result = Stream.iterate(1, i -> i + 1) //Infinite Stream
            .limit(iterations)
            .filter(isPerfect)
            .peek(System.out::println)
            .count();

        //assertThat(result)
        //    .usingComparator(BigDecimal::compareTo)
        //    .isCloseTo(BigDecimal.valueOf(1), within(BigDecimal.valueOf(0.00001)));
    }
}

