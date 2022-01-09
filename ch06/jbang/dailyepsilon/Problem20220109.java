///usr/bin/env jbang "$0" "$@" ; exit $?
//DEPS org.assertj:assertj-core:3.21.0

package ch06.jbang.dailyepsilon;

import java.math.BigDecimal;
import java.math.MathContext;
import java.math.RoundingMode;
import java.time.Duration;
import java.time.Instant;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.within;

public class Problem20220109 {

    public static void main(String[] args) {

        Predicate<Integer> isDivisible_1_to_20 = number -> {
            var counter = IntStream.rangeClosed(1, 20).boxed()
                .map(n -> {
                    if (number % n == 0) {
                        return 1;
                    }
                    return 0;
                })
                .reduce(0, Integer::sum);
            
            return (counter == 20) ? true : false;
        };

        Instant start = Instant.now();

        var result = Stream.iterate(1, i -> i + 1) //Infinite Stream
            .filter(isDivisible_1_to_20)
            .limit(1)
            .peek(System.out::println)
            .map(String::valueOf)
            .map(String::length)
            .findAny()
            .orElseThrow();

        System.out.println(result);

        Instant end = Instant.now();
        System.out.println("Process time: " + Duration.between(start, end).toSeconds() + " seconds"); 

        assertThat(result).isEqualTo(9);
    }
}

