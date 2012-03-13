/**
 * 'Script' for collecting accuracy results in group assignment DMT course.
 * @author Anung Ariwibowo
 * @version 20110405
 */

import weka.core.Attribute;
import weka.core.Instances;
//import weka.core.converters.ConvertUtils.DataSource;
import weka.core.converters.ArffLoader;
import java.io.File;
import java.io.IOException;
import java.util.Random;
//import wlsvm.WLSVM;
import weka.classifiers.bayes.NaiveBayes;               // Naive bayes
import weka.classifiers.functions.SMO;                  // SVM
import weka.classifiers.trees.J48;                      // C4.5
import weka.classifiers.trees.Id3;                      // ID3
import weka.classifiers.trees.SimpleCart;               // CART
import weka.classifiers.functions.MultilayerPerceptron; // NN
import weka.classifiers.Evaluation;
import java.util.Calendar;

public class Jam {
  public static void main (String[] args) throws Exception {
    String datasets[] = {
        "data20120229/MovieReviewOccurrence.arff"               // 0
      , "data20120229/MovieReviewOccurrenceSum.arff"            // 1
      , "data20120229/MovieReviewOccurrenceAvg.arff"            // 2
      , "data20120229/MovieReviewOccurrencePosNeg.arff"         // 3
      , "data20120229/MovieReviewOccurrenceAllScores.arff"      // 4
      , "data20120229/MovieReviewSubjScore.arff"                // 5
      , "data20120229/MovieReviewSubjScoreSum.arff"             // 6
      , "data20120229/MovieReviewSubjScoreAvg.arff"             // 7
      , "data20120229/MovieReviewSubjScorePosNeg.arff"          // 8
      , "data20120229/MovieReviewSubjScoreAllScores.arff"       // 9
      , "data20120229/MovieReviewWeightScore.arff"              // 10
      , "data20120229/MovieReviewWeightScoreSum.arff"           // 11
      , "data20120229/MovieReviewWeightScoreAvg.arff"           // 12
      , "data20120229/MovieReviewWeightScorePosNeg.arff"        // 13
      , "data20120229/MovieReviewWeightScoreAllScores.arff"     // 14
      , "data20120229/MovieReviewAggregate.arff"                // 15
    };
    int ii;
    int jj;
    int ctr;
    int loopLimit;
    loopLimit = datasets.length;
    for (ii=0; ii<10; ii++) {
      Calendar kal = Calendar.getInstance();
      int day = kal.get(Calendar.DATE);
      int month = kal.get(Calendar.MONTH) + 1;
      int year = kal.get(Calendar.YEAR);
      int hour = kal.get(Calendar.HOUR);
      int minute = kal.get(Calendar.MINUTE);
      int second = kal.get(Calendar.SECOND);

      System.out.println("Current date-time: " + kal.getTime());
      System.out.println("HH:MM:SS " + hour + ":" + minute + ":" + second);
      for (jj=0; jj<2; jj++) {
        for (ctr=0; ctr<loopLimit; ctr++) {
          ArffLoader loader = new ArffLoader();
          String dataFile = datasets[ctr];
          System.out.println("Loading data Training ''" + dataFile + "''...");
          loader.setFile(new File(dataFile));
          Instances data = loader.getDataSet();
          data.setClassIndex(data.numAttributes() - 1);
        }
      }
    }
  }
}

