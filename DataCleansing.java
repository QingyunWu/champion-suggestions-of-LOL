import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class DataCleansing {
	public static void main(String[] args) throws Exception { 
		if (args.length != 2) {
	    	System.err.println("Usage: DataCleansing <input path> <output path>");
	      	System.exit(-1);
	    }
		Job job = new Job();
		job.addFileToClassPath(new Path("jarpath/json-20090211.jar")); 
		job.setJarByClass(PageRank.class);
		job.setJobName("DataCleansing");
		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
	    job.setMapperClass(DataCleansing.class);
	    job.setReducerClass(DataCleansing.class);
	    job.setOutputKeyClass(Text.class);
	    job.setOutputValueClass(Text.class);
	    System.exit(job.waitForCompletion(true) ? 0 : 1);
	 }
}         