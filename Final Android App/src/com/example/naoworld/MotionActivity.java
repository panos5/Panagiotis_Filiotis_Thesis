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
import android.graphics.Typeface;
import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.View.OnTouchListener;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;

public class MotionActivity extends Activity {

	//Declaration of instance variables that will be used within the class
	TextView txvHeader;
	ImageButton btHome;
	Button btSpeech;
	Button btSettings;
	Button btSpeechRec;
	Button btBattery;
	Button btDemos;	
	ImageButton btUpArrow;
	ImageButton btDownArrow;
	ImageButton btLeftArrow;
	ImageButton btRightArrow;
	Button btStandUp;
	Button btSitDown;
	Button btTurnLeft;
	Button btTurnRight;

	
	/*
	 * Declaration of instance variables 
	 * @command is an integer which is related on each button functionality.According the button 
	 * is pressed every time the command takes a different value so to help the thread identify which button
	 * has been pressed and proceed with the relevant action
	 */
	private int command=1;
	private HttpGet selectedAction;
	public String addressIP;
	
	SharedPreferences settings; 
	
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_motion);
		
		/* Initializes the font orange to a type face that can be used within 
		 * the class from all elements and methods just by calling and setting 
		 * the type face of the element to tfOrange
		 */		
		Typeface tfOrange = Typeface.createFromAsset(getAssets(),"fonts/orange.ttf");
		
		
		/* Attach Views to all the elements of the GUI
		* @btHome is attached to the button which when is pressed brings up the MainPanel Activity
		* @btSpeech is attached to the button which when is pressed brings up the Speech Activity
		* @btSettings is attached to the button  which when is pressed brings up the Settings Activity
		* @btDemos is attached to the button which when is pressed brings up the UnderConstruction Activity
		* @btBattery is attached to the button which when is pressed brings up the Battery Activity
		* @btSpeechRec is attached to the button which when is pressed brings up the UnderConstruction Activity
		* @btUpArrow is attached to the button corresponds which moves the robot forward
		* @btDownArrow is attached to the button which moves the robot backwards
		* @btLeftArrow is attached to the button which moves the robot left
		* @btRightArrow is attached to the button which moves the robot right
		* @btStandUp is attached to the button which makes the robot stand up
		* @btSitDown is attached to the button which makes the robot sit down
		* @btTurnLeft is attached to the button which makes the robot turn left
		* @btTurnRight is attached to the button which makes the robot turn right
		*/		
	    btHome = (ImageButton) findViewById(R.id.imgbtHome_Motion);
	    btSpeech = (Button) findViewById(R.id.btSpeech_Motion);
	    btSettings = (Button) findViewById(R.id.btSettings_Motion);
	    btDemos = (Button) findViewById(R.id.btDemos_Motion);
	    btBattery = (Button) findViewById(R.id.btBattery_Motion);
	    btSpeechRec = (Button) findViewById(R.id.btSpeechRec_Motion);
	    
	    btUpArrow = (ImageButton) findViewById(R.id.btUp_Motion); 
	    btDownArrow = (ImageButton) findViewById(R.id.btDown_Motion); 
	    btLeftArrow = (ImageButton) findViewById(R.id.btLeft_Motion); 
	    btRightArrow = (ImageButton) findViewById(R.id.btRight_Motion); 
	    
	    btStandUp = (Button) findViewById(R.id.btStandUp_Motion);
	    btSitDown = (Button) findViewById(R.id.btSitDown_Motion);
	    btTurnLeft = (Button) findViewById(R.id.btTurnLeft_Motion);
	    btTurnRight = (Button) findViewById(R.id.btTurnRight_Motion);
	
	    
	    /* Attaches the instance variable txvHeader to the textView(Header of the motion activity) 
	     * of the interface of the Android and the second line sets the font of the element to tfOrange
	     */
		txvHeader = (TextView) findViewById(R.id.txvHeader_Motion);
		txvHeader.setTypeface(tfOrange);
	
		/*
		 * Declaration of the SharedPreferences object and assignment
		 * to the addressIP variable the value that has been stored from settings
		 */
		
		settings = getSharedPreferences( null , MODE_PRIVATE);
		addressIP = (settings.getString("ip", ""));

		
		
		// Create a listener responding when user holds the button down
		// constantly
		// or release it
//		OnTouchListener otlButton = new OnTouchListener() {
//			@Override
//			public boolean onTouch(View v, MotionEvent event) {
//				switch (event.getAction()) {
//				
//				// if you want to handle the touch event
//				case MotionEvent.ACTION_DOWN:
//					
//					for(int i =0;i<10;i++){
//					
//						HttpGet httpMoveForward = new HttpGet("http://"+ addressIP +":9559/?eval"
//							+ "=ALMotion.moveTo(0.05%20,%200,%200)");
//						selectedAction = httpMoveForward ;
//					}
//						break;			
//				case MotionEvent.ACTION_UP:
//					
//					System.out.println(5);
//					break;
//				}
//	           
//	            return false;
//	        }
//	    };
		
	

		/* Creates a runnable interface which includes the method run
		 * and will allow threads to run when is needed by calling the runnable interface itself
		 */
		final Runnable runnable = new Runnable() {
			
	        public void run() {     	
	        		 
	        	try {
	        		  
	        		//Creating an HTTP client
	        		HttpClient httpClient = new DefaultHttpClient();
	        		
	        		if  (command == 1)
        			{			
				    
        			//Creating HTTP Post
					HttpGet httpMoveForward = new HttpGet("http://"+ addressIP +":9559/?eval"
							+ "=ALMotion.moveTo(0.2%20,%200,%200)");
					selectedAction = httpMoveForward ; 						   
        			}
	        		
	        		
	        		else if  (command == 2)
        			{			
				    
        			//Creating HTTP Post
					HttpGet httpMoveBack = new HttpGet("http://"+ addressIP +":9559/?eval"
							+ "=ALMotion.moveTo(-0.2%20,%200,%200)");
					selectedAction = httpMoveBack ; 						   
        			}
	        		
	        		
	        		else if  (command == 3)
        			{			
				    
        			//Creating HTTP Post
					HttpGet httpMoveLeft = new HttpGet("http://"+ addressIP +":9559/?eval"
							+ "=ALMotion.moveTo(0%20,%200.2%20,%200)");
					selectedAction = httpMoveLeft ; 						   
        			}
	        		
	        		
	        		else if  (command == 4)
        			{			
				    
        			//Creating HTTP Post
					HttpGet httpMoveRight = new HttpGet("http://"+ addressIP +":9559/?eval"
							+ "=ALMotion.moveTo(0%20,%20-0.2,%200)");
					selectedAction = httpMoveRight ; 						   
        			}
	        		
	        		
			
	        		else if  (command == 5)
	        			{			
					    
	        			//Creating HTTP Post
						HttpGet httpStandUp = new HttpGet("http://"+ addressIP +":9559/?eval"
								+ "=ALRobotPosture.goToPosture(%22Stand%22,%200.8)");
						selectedAction = httpStandUp ; 						   
	        			}
								
					else if (command == 6) 
							{
						    //Creating HTTP Post
							HttpGet httpSitDown = new HttpGet("http://"+ addressIP +":9559/?eval"
									+ "=ALRobotPosture.goToPosture(%22Sit%22,%200.8)");
							selectedAction = httpSitDown ; 		
							}
					
					else if (command == 7) 
							{
						    //Creating HTTP Post
							HttpGet httpTurnLeft = new HttpGet("http://"+ addressIP +":9559/?eval"
								+ "=ALMotion.moveTo(0%20,%200%20,%201.5709)");
							selectedAction = httpTurnLeft ; 		
							}
					
					else if (command == 8) 
							{
							//Creating HTTP Post
							HttpGet httpTurnRight = new HttpGet("http://"+ addressIP +":9559/?eval"
								+ "=ALMotion.moveTo(0%20,%200%20,%20-1.5709)");
							selectedAction = httpTurnRight ;		
							}
									
						
							try {   
								/* A response is declared and executes each time the action(HttpGet) that
								 * equals the the selectedAction variable.
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
	
	
					
        /* Declares a single click listener which will produce a relevant
         * result every time a different action occurs. e.g user presses a button or 
         * a single click inside an edit text view. 
         */
		OnClickListener oclButton = new OnClickListener() {
			@Override
			public void onClick(View v) {
				// Defines the buttons that invoked the listener by their id
				switch (v.getId()) {
				
				/* Actions related to the buttons displayed on the bottom of the screen
				 * which control the swap between the activities
				 */
				case R.id.imgbtHome_Motion:
					startActivity(new Intent(MotionActivity.this,
							MainPanel.class));
					break;					
				case R.id.btSettings_Motion:
					startActivity(new Intent(MotionActivity.this,
							SettingsActivity.class));
					break;
				case R.id.btSpeech_Motion:
					startActivity(new Intent(MotionActivity.this,
							SpeechActivity.class));
					break;
				case R.id.btDemos_Motion:
					startActivity(new Intent(MotionActivity.this,
							UnderConstructionActivity.class));
					break;
				case R.id.btSpeechRec_Motion:
					startActivity(new Intent(MotionActivity.this,
							UnderConstructionActivity.class));
					break;
				case R.id.btBattery_Motion:		
					 
					break;
					
				/* Actions related to the direction arrows which control the movement of
				 * the robot left,right,up and down.
				 */
				case R.id.btUp_Motion:
					command = 1;
					Thread MoveForwardThread = new Thread(runnable);
					MoveForwardThread.start();					
					break;
				case R.id.btDown_Motion:
					command = 2;
					Thread MoveBackThread = new Thread(runnable);
					MoveBackThread.start();					
					break;
				case R.id.btLeft_Motion:
					command = 3;
					Thread MoveLeftThread = new Thread(runnable);
					MoveLeftThread.start();
					break;
				case R.id.btRight_Motion:
					command = 4;
					Thread MoveRightThread  = new Thread(runnable);
					MoveRightThread.start();
					break;
					
				/* Actions related to the buttons which command the robot to
				 * stand up ,sit down ,turn left and right.
				 */	
				case R.id.btStandUp_Motion:
					command = 5;
					Thread StanduUpThread = new Thread(runnable);
					StanduUpThread.start();					
					break;
				case R.id.btSitDown_Motion:
					command = 6;
					Thread SitDownThread = new Thread(runnable);
					SitDownThread.start();
					break;
				case R.id.btTurnLeft_Motion:
					command = 7;
					Thread TurnRightThread = new Thread(runnable);
					TurnRightThread.start();					
					break;
				case R.id.btTurnRight_Motion:
					command = 8;
					Thread TurnLeftThread = new Thread(runnable);
					TurnLeftThread.start();					
					break;
					
				}
			}
	     };
	 
	     
	     // Assignment of the Click listener event to each button separately
	     btHome.setOnClickListener(oclButton);
         btSettings.setOnClickListener(oclButton);
	     btSpeech.setOnClickListener(oclButton);
	     btDemos.setOnClickListener(oclButton);
	     btSpeechRec.setOnClickListener(oclButton);
	     btBattery.setOnClickListener(oclButton);
	     
	     btUpArrow.setOnClickListener(oclButton);
	     btDownArrow.setOnClickListener(oclButton);
	     btLeftArrow.setOnClickListener(oclButton);
	     btRightArrow.setOnClickListener(oclButton);
	     
	     
	     btStandUp.setOnClickListener(oclButton);
   	 	 btSitDown.setOnClickListener(oclButton);
	 	 btTurnLeft.setOnClickListener(oclButton);
	 	 btTurnRight.setOnClickListener(oclButton);
	     
	 	 
	     
//	     btUpArrow.setOnTouchListener(otlButton);
//	     btDownArrow.setOnTouchListener(otlButton);
//	     btLeftArrow.setOnTouchListener(otlButton);
//	     btRightArrow.setOnTouchListener(otlButton);
	     
	         
	     
	}
	
}
