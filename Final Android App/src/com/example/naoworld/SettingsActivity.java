package com.example.naoworld;

import java.io.IOException;

import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.Typeface;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.view.WindowManager;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.SeekBar;
import android.widget.Toast;
import android.widget.SeekBar.OnSeekBarChangeListener;
import android.widget.TextView;

public class SettingsActivity extends Activity {
	
	//Declaration of instance variables(buttons,textViews) used within the class
	TextView txvHeader;
	TextView txvSubHeader;	
	TextView txvChangeIP;
	TextView txvChangeName;
	TextView txvBatteryLevel;
	
	Button btMotion;
	Button btSpeech;
	ImageButton imgHome;
	Button btSpeechRec;
	Button btBattery;
	Button btDemos;
	
	Button btChangeName;
	Button btChangeIP;
	Button btTestSound;
	
	TextView txvCurrentSettings;	
	TextView txvRobotName;	
	TextView txvIPAddress;
	TextView txvSoundVolume;
	TextView txvRobotNameVal;
	TextView txvIPVal;
	TextView txvSoundVal;
	
	ImageView imgBattery;
	
	SeekBar skbSoundModify;
	
	int stepSound = 10;
	int maxSound = 100;
	int minSound = 0;
	
	public String addressIP = "192.168.0.4";
	private int command=0;
	private HttpGet selectedAction;
	private int soundsScale;
	
	SharedPreferences settings;	
	SharedPreferences.Editor prefEditor;
	
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_settings);
		
		//Doesn't allow the edit texts to take focus and keeps the keyboard hidden
		getWindow().setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_STATE_HIDDEN);
		
		Typeface tfOrange = Typeface.createFromAsset(getAssets(),"fonts/orange.ttf");
		
		settings = getSharedPreferences(null,MODE_PRIVATE);	
		prefEditor= settings.edit();
			

		/* Attach Views to all the elements of the GUI
		* @imgHome is attached to the button which when is pressed brings up the MainPanel Activity
		* @imgBattery
		* @btSpeech is attached to the button which when is pressed brings up the Speech Activity
		* @btMotion is attached to the button  which when is pressed brings up the Motion Activity
		* @btDemos is attached to the button which when is pressed brings up the UnderConstruction Activity
		* @btBattery is attached to the button which when is pressed brings up the Battery Activity
		* @btSpeechRec is attached to the button which when is pressed brings up the UnderConstruction Activity
		* @btChangeName is attached to the button which changes the name of the robot regarding the inserted value
		* @btChangeIP is attached to the button which changes the IP of the robot regarding the inserted value
		* @btTestSound is attached to the button which test the volume of the sound
		* @txvChangeName is attached to the text view holds the value of the new name provided by the user
		* @txvChangeIP is attached to the text view holds the value of the new IP provided by the user
		* @txvCurrentSettings 
	    * @txvRobotName 
	    * @txvIPAddress 
	    * @txvSoundVolume
	    * @txvRobotNameVal
	    * @txvIPVal 
	    * @txvSoundVal 
		*/
		imgHome = (ImageButton) findViewById(R.id.imgbtHome_Settings);
		imgBattery = (ImageView) findViewById(R.id.imgBattery);
		txvBatteryLevel = (TextView) findViewById(R.id.txvBatteryLevel);

		btSpeech = (Button) findViewById(R.id.btSpeech_Settings);
		btMotion = (Button) findViewById(R.id.btMotion_Settings);
		btDemos = (Button) findViewById(R.id.btDemos_Settings);
	    btBattery = (Button) findViewById(R.id.btBattery_Settings);
	    btSpeechRec = (Button) findViewById(R.id.btSpeechRec_Settings);
	    
		btChangeName = (Button) findViewById(R.id.btChangeName_Settings);
		btChangeIP = (Button) findViewById(R.id.btChangeIP_Settings);
	    btTestSound = (Button) findViewById(R.id.btTestSound_Settings);
		
		txvChangeName = (TextView) findViewById(R.id.txvChangeName_Settings);
	    txvChangeIP = (TextView) findViewById(R.id.txvChangeIP_Settings);
	    
	    txvCurrentSettings = (TextView) findViewById(R.id.txvCurrentSet_Settings);
	    txvRobotName = (TextView) findViewById(R.id.txvRobotName_Settings);
	    txvIPAddress = (TextView) findViewById(R.id.txvIP_Settings);
	    txvSoundVolume = (TextView) findViewById(R.id.txvSound_Settings);
	    txvRobotNameVal = (TextView) findViewById(R.id.txvRobotName_val);
	    txvIPVal = (TextView) findViewById(R.id.txvIP_val);
	    txvSoundVal = (TextView) findViewById(R.id.txvSound_val);
	   
	    
	    /* Attaches the instance variable txvHeader to the textView(Header of the motion activity) 
	     * of the interface of the Android and the second line sets the font of the element to tfOrange
	     */
		txvHeader = (TextView) findViewById(R.id.txvHeader_Settings);
		txvHeader.setTypeface(tfOrange);
		
		
		/* Attaches the instance variable sbkSoundModify to the seek bar which adjusts the volume fo the sound 
	     * Also is defined the maximum value that the sound can reach
	     */
		skbSoundModify = (SeekBar) findViewById(R.id.barSoundModify_Settings);
		skbSoundModify.setMax( (maxSound - minSound) / stepSound );
		
		setValues();
		checkBattery();
		
		/* Creates a runnable interface which includes the method run
		 * and will allow threads to run when is needed by calling the runnable interface itself
		 */
		final Runnable runnable = new Runnable() {
			
	        public void run() {     	
	        		 
	        	try {
	        		  
	        		//Creating an HTTP client
	        		HttpClient httpClient = new DefaultHttpClient();
	        		
	        		if (command == 1)
        			{			
				    
        			//Creating HTTP Post
					HttpGet httpCheckConnection = new HttpGet("http://"+ addressIP +":9559/?eval"
							+ "=ALMemory.ping()");
					selectedAction = httpCheckConnection ; 						   
        			}
	        		
	        		
	        		else if (command == 2)
        			{			
				    
        			//Creating HTTP Post
					HttpGet httpAdjustSound = new HttpGet("http://"+ addressIP +":9559/?eval"
							+ "=ALAudioDevice.setOutputVolume(" + Integer.toString(soundsScale) +")");
					selectedAction = httpAdjustSound ; 						   
        			}
	        		
	        		else if (command == 3)
        			{			
				    
        			//Creating HTTP Post
					HttpGet httpTestSound = new HttpGet("http://"+ addressIP +":9559/?eval"
							+ "=ALTextToSpeech.say(%22Test%20the%20Volume%22)");
					selectedAction = httpTestSound ; 						   
        			}
	        										
						try {   
							/* A response is declared and executes each time the action that
							 * the selectedAction variable defines.
							 * Afterwards the response is converted to a string and can be used
							 * everywhere in the application is needed
							 */
							HttpResponse response = httpClient.execute(selectedAction);
							String responseBody = EntityUtils.toString(response.getEntity());
							System.out.println(responseBody);								 
							} 
						
						catch (ClientProtocolException e) 
							{
							// writing exception to log
						    e.printStackTrace();								         
							}				
					
						catch (IOException e) 
							{
							// writing exception to log
						    e.printStackTrace();
							}
			     				        }
		  
			    catch (Exception e) {}
			        		
			        }
				
			};
			
		
		//Creates a listener for the adjustments of the seek bar
		skbSoundModify.setOnSeekBarChangeListener(
		    new OnSeekBarChangeListener()
		    {
		        @Override
		        public void onStopTrackingTouch(SeekBar seekBar) {}

		        @Override
		        public void onStartTrackingTouch(SeekBar seekBar) {}

		        @Override
		        public void onProgressChanged(SeekBar seekBar, int progress, 
		            boolean fromUser) 
		        {
		        	
		        	command =2;
		        	soundsScale = minSound + (progress * stepSound);
		        	Thread AdjustSoundThread = new Thread(runnable);
		        	AdjustSoundThread.start();
		          	//String responseBody = EntityUtils.toString(response.getEntity());

		            prefEditor.putString("sound", Integer.toString(soundsScale));	
		            prefEditor.commit();
		            txvSoundVal.setText(Integer.toString(soundsScale) + "%");
		        	
		            

		        }
		    }
		);
		
		
	    
	   /* Declaration of a single click listener which will produce a relevant
       * result every time a different action occurs. e.g user presses a button or 
       * a single click inside an edit text view. 
       */
	   OnClickListener oclButton = new OnClickListener() {
	   @Override
       public void onClick(View v) {
	 		// define the button that invoked the listener by id
	 		switch (v.getId()) {
	 			case R.id.imgbtHome_Settings:
					startActivity(new Intent(SettingsActivity.this , MainPanel.class));
	 				break;
	 			case R.id.btSpeech_Settings:
	 				startActivity(new Intent(SettingsActivity.this , SpeechActivity.class));
	 				break;
	 			case R.id.btMotion_Settings:
					startActivity(new Intent(SettingsActivity.this , MotionActivity.class));
	 				break;
	 			case R.id.btSpeechRec_Settings:
	 				startActivity(new Intent(SettingsActivity.this,
							UnderConstructionActivity.class));
	 				break;
	 			case R.id.btDemos_Settings:
	 				startActivity(new Intent(SettingsActivity.this,
							UnderConstructionActivity.class));
	 				break;
	 			case R.id.btBattery_Settings:	
	 				 				
	 				break;
	 				
	 			
	 			case R.id.txvChangeIP_Settings:
	 				txvChangeIP.setTextColor(Color.parseColor("#ffffff"));
	 				txvChangeIP.setText("");
	 				break;
	 			
	 			case R.id.txvChangeName_Settings:
	 				txvChangeName.setTextColor(Color.parseColor("#ffffff"));
	 				txvChangeName.setText("");
	 				break;
	 				
	 			
	 			case R.id.btChangeName_Settings:
	 				
	 				if (txvChangeName.length() == 0){
					
	 					txvChangeName.setTextColor(Color.parseColor("#ffff0000"));
	 					txvChangeName.setText("Please enter a valid name..");
	
					}
					else if(txvChangeName.getText().toString().equals("Enter a new name")){
						
						txvChangeName.setTextColor(Color.parseColor("#ffff0000"));
					}
					
					else {
						
						txvRobotNameVal.setText(txvChangeName.getText().toString());
						prefEditor.putString("name",txvChangeName.getText().toString());	

						boolean flag = prefEditor.commit();
					    			    
						if(flag==true)
						{
							Toast toast = Toast.makeText(getApplicationContext(),
									"The name changed sucessfully!",
									Toast.LENGTH_LONG);
							toast.setGravity(Gravity.TOP, 0, 400);
							toast.show();
						}
						
//						Thread speakThread = new Thread(runnable);
//						speakThread .start();
					} 				
	 				break;
	 			
	 				
	 			case R.id.btChangeIP_Settings:
	 				if (txvChangeIP.length() == 0){
						
	 					txvChangeIP.setTextColor(Color.parseColor("#ffff0000"));
	 					txvChangeIP.setText("Please enter a valid IP..");
	
					}
					else if(txvChangeIP.getText().toString().equals( "Enter an IP address")){
						
						txvChangeIP.setTextColor(Color.parseColor("#FF0033"));
					}
					
					else {
						
						txvIPVal.setText(txvChangeIP.getText().toString());
						prefEditor.putString("ip",txvChangeIP.getText().toString());	
						boolean flag = prefEditor.commit();
					    			    
//						if(flag==true)
//						{
//							Toast toast = Toast.makeText(getApplicationContext(),
//									"Robot has been connected sucessfully!",
//									Toast.LENGTH_LONG);
//							toast.setGravity(Gravity.TOP, 0, 600);
//							toast.show();
//						}
						
					}

	 				break;
	 			case R.id.btTestSound_Settings:
	 				
	 				command = 3;
					Thread TestSoundThread = new Thread(runnable);
					TestSoundThread.start();
	 				
	 				
	 				break;
	}
	
		}
	     };
     
	     // assign click listener to the OK button (btnOK)
	     btMotion.setOnClickListener(oclButton);
	     imgHome.setOnClickListener(oclButton);
	     btSpeech.setOnClickListener(oclButton);
	     btDemos.setOnClickListener(oclButton);
	     btBattery.setOnClickListener(oclButton);
	     btSpeechRec.setOnClickListener(oclButton);
	     
	     txvChangeIP.setOnClickListener(oclButton);
	     txvChangeName.setOnClickListener(oclButton);
	     
	     btChangeName.setOnClickListener(oclButton);
	     btChangeIP.setOnClickListener(oclButton);
	     btTestSound.setOnClickListener(oclButton);
  
	    
	}
	 
	public void setValues(){
		  
		String robotName = settings.getString("name","");
		String robotIP = settings.getString("ip","");
		String robotVolume = settings.getString("sound","");
		
		if (robotName.equals("")){ }

		else
		{
			txvRobotNameVal.setText(robotName);
		}
		
		if (robotIP.equals("")){ }

		else
		{
			txvIPVal.setText(robotIP);
		}
		
		if (robotVolume.equals("")){ }

		else
		{
			skbSoundModify.setProgress(Integer.parseInt(robotVolume) / 10);
			txvSoundVal.setText(robotVolume + "%");
		}
	
	}
	
	
	
	public void checkBattery(){
		
		
		
		if(txvSoundVal.getText().toString().equals("20%")){
			
			imgBattery.setImageResource(R.drawable.battery_empty);
			
		}
		
		else if(txvSoundVal.getText().toString().equals("40%")){
			
			imgBattery.setImageResource(R.drawable.battery_bottom_half);
			
				}
		
		else if(txvSoundVal.getText().toString().equals("60%")) {
			
			imgBattery.setImageResource(R.drawable.battery_half);
			
				}
		
		
		else if(txvSoundVal.getText().toString().equals("80%")) {
	
			imgBattery.setImageResource(R.drawable.battery_top_half);
	
		     }
		
		else {
	
			imgBattery.setImageResource(R.drawable.battery_full);
	
			}
		
		txvBatteryLevel.setText(txvSoundVal.getText().toString());
			
		
	}	  
		  
	 		
}
