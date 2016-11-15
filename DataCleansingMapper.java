import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;
import org.apache.hadoop.io.*;
import org.json.*;


public class DataCleansingMapper extends Mapper<LongWritable, Text, Text, Text> {
	@Override
	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
		String line = value.toString();
		int playerID = 0;
		int championID = 0;
		int championPoints = 0; 
        try {
        	JSONObject obj = new JSONObject(line);
        	playerID = obj.getInt("playerId");
        	championID = obj.getInt("championId");
        	championPoints = obj.getInt("championPoints");
        	context.write(new Text(String.valueOf(playerID)), new Text(String.valueOf(championID) + "," + String.valueOf(championPoints)));
        } catch (JSONException e) {
        	e.printStackTrace();
        }
		
	}
}
