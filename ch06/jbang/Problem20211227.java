package ch06.jbang;

import java.math.BigDecimal;
import java.math.MathContext;
import java.math.RoundingMode;
import java.util.stream.IntStream;

public class Problem20211227 {

    public static void main(String[] args) {
        
        var iterations = 100;
        var precision = new MathContext(10); // 10 Digits of precision
        var roundingMode = RoundingMode.HALF_UP; // Rounding mode

        var result = IntStream.range(1, iterations).boxed()
            .map(n -> {
                return BigDecimal.valueOf(4 * n).divide(
                    BigDecimal.valueOf(3).pow(n - 2, precision), roundingMode);
            })
            .reduce(BigDecimal.ZERO, BigDecimal::add)
            .longValue(); 
        
        System.out.println(result);
    }
}
