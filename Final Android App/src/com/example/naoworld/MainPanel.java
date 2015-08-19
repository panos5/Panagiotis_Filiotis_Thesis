package com.example.naoworld;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Typeface;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;

public class MainPanel extends Activity {
	
	//Declaration of instance variables that will be used within the class
	Button btMotion;
	Button btSpeech;
	Button btSettings;
	TextView txvheader;
	Button btSpeechRec;
    Button btDemos;
	Button btBattery;
	

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_login);
		
		/* Assigns the font orange to a type face that can be used within 
		 * the class from all elements just by calling and setting 
		 * the type face of each element to tfOrange
		 */
		Typeface tfOrange = Typeface.createFromAsset(getAssets(),"fonts/orange.ttf");

		
		/* Attach Views to all the elements of the GUI
		* @btHome is attached to the button which when is pressed brings up the MainPanel Activity
		* @btSpeech is attached to the button which when is pressed brings up the Speech Activity
		* @btSettings is attached to the button  which when is pressed brings up the Settings Activity
		* @btDemos is attached to the button which when is pressed brings up the UnderConstruction Activity
		* @btBattery is attached to the button which when is pressed brings up the Battery Activity
		* @btSpeechRec is attached to the button which when is pressed brings up the UnderConstruction Activity
		* @btBattery is attached to the button which when is pressed brings up the Battery Activity
	    */
	    btMotion = (Button) findViewById(R.id.btMotion_LogIn);
	    btSpeech = (Button) findViewById(R.id.btSpeech_LogIn);
	    btSettings = (Button) findViewById(R.id.btSettings_LogIn);
	    btSpeechRec = (Button) findViewById(R.id.btSpeechRec_LogIn);
	    btDemos = (Button) findViewById(R.id.btDemos_LogIn);
	    btBattery = (Button) findViewById(R.id.btBattery_LogIn);
	    
	    
	    /* Attaches the instance variable txvHeader to the textView(Header of the MainPanel activity) 
	     * of the interface  and the second line sets the font of the element to tfOrange
	     */
	    txvheader = (TextView) findViewById(R.id.txvMainTitle_LogIn);
	    txvheader.setTypeface(tfOrange);
	    
	
        /* Creates an object of a single click listener called oclButon
         * and includes a method in which depending what happens
         * on each click a relevant action occurs
         */
		OnClickListener oclButton = new OnClickListener() {
			@Override
			public void onClick(View v) {
				// define the button that invoked the listener by id
				switch (v.getId()) {
				
				/*
				 * On each click of a button a new activity comes in front
				 */
				case R.id.btMotion_LogIn:
					startActivity(new Intent(MainPanel.this,
							MotionActivity.class));
					break;					
				case R.id.btSettings_LogIn:
					startActivity(new Intent(MainPanel.this,
							SettingsActivity.class));
					break;
				case R.id.btSpeech_LogIn:
					startActivity(new Intent(MainPanel.this,
							SpeechActivity.class));
					break;
				case R.id.btSpeechRec_LogIn:
					startActivity(new Intent(MainPanel.this,
							UnderConstructionActivity.class));
					break;
				case R.id.btDemos_LogIn:
					startActivity(new Intent(MainPanel.this,
							UnderConstructionActivity.class));
					break;
				case R.id.btBattery_LogIn:
					startActivity(new Intent(MainPanel.this,
							UnderConstructionActivity.class));
					break;
					
				}
			}
	     };
	 
	  // Assignment of the Click listener event to each button separately	     
	     btMotion.setOnClickListener(oclButton);
         btSettings.setOnClickListener(oclButton);
	     btSpeech.setOnClickListener(oclButton);
	     btSpeechRec.setOnClickListener(oclButton);
	     btDemos.setOnClickListener(oclButton);
	     btBattery.setOnClickListener(oclButton);
	}

}
