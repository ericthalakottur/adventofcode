import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;

class Solution {
    public static void main(String args[]) {

        try (BufferedReader br = new BufferedReader(new FileReader(args[0]))) {
            AtomicInteger answer1 = new AtomicInteger();
            AtomicInteger answer2 = new AtomicInteger();

            br.lines()
                    .forEach(line -> {
                        List<Integer> data = Arrays.stream(line.split(" "))
                                .map(Integer::parseInt)
                                .toList();

                        boolean reportSafe = isReportSafe(data);
                        answer1.addAndGet(reportSafe? 1 : 0);

                        if (reportSafe) {
                            answer2.addAndGet(1);
                            return;
                        }

                        for (int i = 0; i < data.size(); i++) {
                            List<Integer> tmp = new ArrayList<>(data);
                            tmp.remove(i);

                            reportSafe = isReportSafe(tmp);

                            if (reportSafe) {
                                answer2.addAndGet(1);
                                return;
                            }
                        }
                    });

            System.out.println("Answer 1: " + answer1);
            System.out.println("Answer 2: " + answer2);
        } catch (FileNotFoundException fileNotFoundException) {
            System.err.println("Error: File not found");
        } catch (Exception exception) {
            System.err.println("Error reading data from file: " + exception);
        }
    }

    private static boolean isReportSafe(List<Integer> data) {
        List<Integer> parsedData = IntStream.range(0, data.size() - 1)
                .map(i -> data.get(i + 1) - data.get(i))
                .boxed()
                .toList();
        return parsedData.stream().allMatch(i -> 1 <= i && i <= 3)
                || parsedData.stream().allMatch(i -> -3 <= i && i <= -1);
    }
}
