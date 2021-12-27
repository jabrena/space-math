package ch06.jbang;

import java.util.stream.IntStream;

/**
 * https://en.wikipedia.org/wiki/Quinary
 */
public class Problem20211224 {

    private static String baseConversion(String number, int sBase, int dBase) {
        // Parse the number with source radix
        // and return in specified radix(base)
        return Integer.toString(
            Integer.parseInt(number, sBase), dBase);
    }

    public static void main(String[] args) {
        
        var iterations = 1000;
        var digitLimit = 2;

        IntStream.range(1, iterations).boxed()
            .map(String::valueOf)
            .map(n -> {
                var result = baseConversion(n, 10, 5);
                System.out.println(n + " " + result);
                return result;
            })
            .takeWhile((s) -> s.length() <= digitLimit)
            .forEach(System.out::println);
    }
}
