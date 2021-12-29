///usr/bin/env jbang "$0" "$@" ; exit $?
//DEPS org.assertj:assertj-core:3.21.0

package ch06.jbang;

import java.math.BigDecimal;
import java.util.function.Function;
import java.util.stream.IntStream;

import static org.assertj.core.api.Assertions.assertThat;

public class Problem20211229 {

    public static void main(String[] args) {
        
        Function<Long, BigDecimal> factorial = limit -> IntStream.iterate(limit.intValue(), i -> i - 1)
                .limit(limit)
                .mapToObj(BigDecimal::valueOf)
                .reduce((n1, n2) -> n1.multiply(n2)).get();

        Double component1 = factorial.apply(11L).doubleValue() / factorial.apply(22L).doubleValue();
        Double component2 = factorial.apply(21L).doubleValue() / factorial.apply(10L).doubleValue();
        Double component3 = Double.valueOf(58);
        Double result = component1 * component2 * component3;

        assertThat(result).as("Result is: ").isEqualTo(29);
    }
}
