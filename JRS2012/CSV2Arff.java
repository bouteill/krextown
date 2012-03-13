import weka.core.Instances;
import weka.core.converters.ArffSaver;
import weka.core.converters.CSVLoader;
 
import java.io.File;
import java.util.Calendar;
 
public class CSV2Arff {
  /**
   * takes 2 arguments:
   * - CSV input file
   * - ARFF output file
   */
  public static void main(String[] args) throws Exception {
    if (args.length != 2) {
      System.out.println("\nUsage: CSV2Arff <input.csv> <output.arff>\n");
      System.exit(1);
    }
 
    // set-up Calendar
    Calendar kal = Calendar.getInstance();
    int day = kal.get(Calendar.DATE);
    int month = kal.get(Calendar.MONTH) + 1;
    int year = kal.get(Calendar.YEAR);
    int hour = kal.get(Calendar.HOUR);
    int minute = kal.get(Calendar.MINUTE);
    int second = kal.get(Calendar.SECOND);

    System.out.println("Current date-time: " + kal.getTime());
    System.out.println("HH:MM:SS " + hour + ":" + minute + ":" + second);

    // load CSV
    CSVLoader loader = new CSVLoader();
    loader.setSource(new File(args[0]));
    System.out.println ("Loading csv data...");
    Instances data = loader.getDataSet();
 
    System.out.println("Current date-time: " + kal.getTime());
    System.out.println("HH:MM:SS " + hour + ":" + minute + ":" + second);

    // save ARFF
    ArffSaver saver = new ArffSaver();
    saver.setInstances(data);
    saver.setFile(new File(args[1]));
    saver.setDestination(new File(args[1]));
    System.out.println ("Saving arff data...");
    saver.writeBatch();

    System.out.println("Current date-time: " + kal.getTime());
    System.out.println("HH:MM:SS " + hour + ":" + minute + ":" + second);

  }
}
