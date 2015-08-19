package com.example.naoworld;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.Typeface;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.text.TextUtils;
import android.view.Gravity;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.WindowManager;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

public class SpeechActivity extends Activity {

	// Declaration of instance variables(buttons,textViews) used within the
	// class
	private TextView txvHeader;
	private Button btMotion;
	private ImageButton imgHome;
	private Button btSettings;
	private Button btSpeak;
	private Button btClearList;
	private Button btAddPhrase;
	private Button btBattery;
	private Button btDemos;
	private Button btSpeechRec;
	private EditText etxManPhrase;
	private ListView lstvPhrases;
	private ArrayList<String> phrases;
	private ArrayAdapter<String> adapter;
	private HashSet<String> setPhrases;

	// Declaring the IP address of the robot
	public String addressIP;

	SharedPreferences savedPhrases;
	SharedPreferences.Editor phrasesEditor;	
	SharedPreferences settings; 
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {

		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_speech);

		// Doesn't allow the edit texts to take focus and keeps the keyboard
		// hidden
		getWindow().setSoftInputMode(
				WindowManager.LayoutParams.SOFT_INPUT_STATE_HIDDEN);

		// Custom Font used for the header of the window
		Typeface tfOrange = Typeface.createFromAsset(getAssets(),
				"fonts/orange.ttf");

		/*
		 * Attach Views to all the elements of the GUI
		 * @imgHome is attached to the button which when is pressed brings up the MainPanel Activity 
		 * @btSettings is attached to the button which when is pressed brings up the Settings Activity
		 * @btMotion is attached to the button which when is pressed brings up the Motion Activity
		 * @btDemos is attached to the button which when is pressed brings up the UnderConstruction Activity
		 * @btBattery is attached to the button which when is pressed brings up the Battery Activity
		 * @btSpeechRec is attached to the button which when is pressed brings up the UnderConstruction Activity
		 * @btSpeak is attached to the button which when is pressed makes the robot speak depending the value of etxManPhrase
		 * @btAddphrase is attached to the button which when is pressed adds the value of etxManPhrase to the list of the Activity 
		 * @etxManPhrase is attached to the text view which holds the value that is provided by the user regarding what he wants the robot to say
		 * @lstPhrases is attached to the list view that holds all the phrases that the user has selected to add
		 */
		imgHome = (ImageButton) findViewById(R.id.imgbtHome_Speech);
		btSettings = (Button) findViewById(R.id.btSettings_Speech);
		btMotion = (Button) findViewById(R.id.btMotion_Speech);
		btDemos = (Button) findViewById(R.id.btDemos_Speech);
		btBattery = (Button) findViewById(R.id.btBattery_Speech);
		btSpeechRec = (Button) findViewById(R.id.btSpeechRec_Speech);

		btSpeak = (Button) findViewById(R.id.btSpeak_Speech);
		btAddPhrase = (Button) findViewById(R.id.btAddPhrase);
		etxManPhrase = (EditText) findViewById(R.id.etxManualPhrase);
		lstvPhrases = (ListView) findViewById(R.id.lstPhrases_Speech);
		btClearList = (Button) findViewById(R.id.btClearList);

		
		/*
		 * Attaches the instance variable txvHeader to the textView(Header of
		 * the motion activity) of the interface of the Android and the second
		 * line sets the font of the element to tfOrange
		 */
		txvHeader = (TextView) findViewById(R.id.txvHeader_Speech);
		txvHeader.setTypeface(tfOrange);

		
		// Declaration of a list of Strings which holds the predefined phrases
		phrases = new ArrayList<String>();
		adapter = new ArrayAdapter<String>(SpeechActivity.this,
				android.R.layout.simple_list_item_1, phrases);
		// Here the data is set in the ListView(lstPhrases)
		lstvPhrases.setAdapter(adapter);

		
		savedPhrases = getPreferences(MODE_PRIVATE);
		phrasesEditor = savedPhrases.edit();
		
		//settings = PreferenceManager.getDefaultSharedPreferences(getBaseContext());
		settings = getSharedPreferences(null,MODE_PRIVATE);

		setPhrases = new HashSet<String>();
		
		// To initialize the values of the IP and lstPhrases variables
		setIP_Phrases();

		
		
		/*
		 * Creating a runnable interface which includes the method run and will
		 * allow threads to run when is asked(e.g in case a button is pressed an
		 * action occurs) by calling the runnable interface
		 */
		final Runnable runnable = new Runnable() {

			public void run() {

				System.out.println(etxManPhrase.getText().toString());

				try {

					/*
					 * The text which is inserted by the user has been modified
					 * before sent to the robot, in order to be acceptable. When
					 * the HttpRequest will be sent then the robot can express
					 * all the words which included to the message, that the
					 * user has typed. If there are gaps between the words the
					 * request can't separate them and see them as unique words.
					 * So initially the text's dots removed and then the gaps
					 * replaced by &20 ,a special character that merges
					 * everything together so the request have a sequence within
					 * the words and the message can be successfully reproduced.
					 */
					String initialText = etxManPhrase.getText().toString();
					String replaceDots = initialText.replace(".", "").trim();
					String finalText = replaceDots.replace(" ", "%20");

					// Creating an HTTP client
					HttpClient httpClient = new DefaultHttpClient();

					// Creating HTTP Post
					HttpGet sayTheWord = new HttpGet("http://" + addressIP
							+ ":9559/?eval" + "=ALTextToSpeech.say(%22"
							+ finalText + "%22)");

					/*
					 * Declaration of an Httpresponse which executes each time
					 * the action that the HttpGet request defines
					 */
					HttpResponse response = httpClient.execute(sayTheWord);

				}

				catch (ClientProtocolException e) {
					// writing exception to log
					e.printStackTrace();
				}

				catch (IOException e) {
					// writing exception to log
					e.printStackTrace();
				}

				catch (Exception e) {
				}

			}

		};

		/*
		 * Declaration of a single click listener which will get the value of
		 * the selected item of the list and put it on the edit text called
		 * etxManPhrase
		 */
		lstvPhrases.setOnItemClickListener(new OnItemClickListener() {
			public void onItemClick(AdapterView<?> myAdapter, View myView,
					int position, long mylng) {
		
				String selectedFromList = (String) (lstvPhrases
						.getItemAtPosition(position));
				etxManPhrase.setText(selectedFromList);
				Thread speakListThread = new Thread(runnable);
				speakListThread.start();
				

			}
		});
		
		
		

		/*
		 * Declaration of a single click listener which will produce a relevant
		 * result every time a different action occurs triggered by the user.
		 * for example the user presses a button or a single click inside an
		 * edit text view.
		 */
		OnClickListener oclButton = new OnClickListener() {
			@Override
			public void onClick(View v) {

				// Defines the button that invoked the listener by id
				switch (v.getId()) {

				/*
				 * Actions related to the buttons displayed on the bottom of the
				 * screen which control the swap between the activities
				 */
				case R.id.imgbtHome_Speech:
					startActivity(new Intent(SpeechActivity.this,
							MainPanel.class));
					break;

				case R.id.btMotion_Speech:
					startActivity(new Intent(SpeechActivity.this,
							MotionActivity.class));
					break;

				case R.id.btSettings_Speech:
					startActivity(new Intent(SpeechActivity.this,
							SettingsActivity.class));
					break;

				case R.id.btSpeechRec_Speech:
					startActivity(new Intent(SpeechActivity.this,
							UnderConstructionActivity.class));
					break;
				case R.id.btDemos_Speech:
					startActivity(new Intent(SpeechActivity.this,
							UnderConstructionActivity.class));
					break;
				case R.id.btBattery_Speech:

					break;

				case R.id.btClearList:
					
					if (phrases.size() == 0)
					
					{
					toastMessage("List is empty");						
					}
					
					else
					{
					adapter.clear();
					adapter.notifyDataSetChanged();
					phrasesEditor.clear();
					phrasesEditor.commit();
					toastMessage("List cleared successfully");
					
					}
					break;

				case R.id.etxManualPhrase:

					etxManPhrase.setTextColor(Color.parseColor("#ffffff"));
					if (etxManPhrase.getText().toString()
							.equals("Please enter your text here...")) {
						etxManPhrase.setText("");
					} else {
					}

					break;

				/*
				 * Actions related to the buttons which are responsible to make
				 * the robot speak and add any phrases in the list for future
				 * use.
				 */
				case R.id.btSpeak_Speech:

					/*
					 * Checks some conditions related to the content of the edit
					 * text The first condition checks if the field is empty
					 * ,secondly if the user has left it with the phrase
					 * "Please enter your text here...".In both cases a warning
					 * message informs the user that has to fill the field in
					 * order to proceed with a relevant action.
					 */
					if (etxManPhrase.length() == 0) {

						etxManPhrase
								.setTextColor(Color.parseColor("#ffff0000"));
						etxManPhrase.setText("Please enter your text here...");
						toastMessage("Edit Text is empty");

					} else if (etxManPhrase.getText().toString()
							.equals("Please enter your text here...")) {

						etxManPhrase
								.setTextColor(Color.parseColor("#ffff0000"));
					}

					// In this case a new thread is created and runs
					else {
						
						Thread speakThread = new Thread(runnable);
						speakThread.start();
					}

					break;

				/*
				 * Check different conditions on clicking of AddPhrase button*
				 * If editText is empty a message pop-up informing the user to
				 * enter a text in the area* If editText is empty a message
				 * pop-up informing the user to enter a text in the area
				 */
				case R.id.btAddPhrase:

					if (etxManPhrase.length() == 0) {

						etxManPhrase
								.setTextColor(Color.parseColor("#ffff0000"));
						etxManPhrase.setText("Please enter your text here...");
						// toastMessage("Edit Text is empty");

					} else if (etxManPhrase.getText().toString()
							.equals("Please enter your text here...")) {

						etxManPhrase
								.setTextColor(Color.parseColor("#ffff0000"));
					}

					else {

				
							
							if (phrases.contains(etxManPhrase.getText()
									.toString())) {

								toastMessage("Phrase is already in the list");
								
							}

							else {

								// Adds the data of the EditText and puts in the
								// array
								phrases.add(etxManPhrase.getText().toString());
								// Check if the adapter has changed and if yes
								// is notified with the new values
								adapter.notifyDataSetChanged();

								setPhrases.addAll(phrases);
								phrasesEditor.putStringSet("phrases",
										setPhrases);
								phrasesEditor.commit();
								toastMessage("Phrase added successfully");

							}
							
							}
					
					break;
				}
				
			}

		};

		// Attach one click listeners to buttons
		imgHome.setOnClickListener(oclButton);
		btMotion.setOnClickListener(oclButton);
		btSettings.setOnClickListener(oclButton);
		etxManPhrase.setOnClickListener(oclButton);
		btAddPhrase.setOnClickListener(oclButton);
		btDemos.setOnClickListener(oclButton);
		btBattery.setOnClickListener(oclButton);
		btSpeechRec.setOnClickListener(oclButton);
		btSpeak.setOnClickListener(oclButton);
		btClearList.setOnClickListener(oclButton);

	}

	
	
	/*
	 * Creates a pop-up(toast) message* @text parameter that defines the text
	 * that will displayed on the pop up window
	 */
	private void toastMessage(String text) {

		Toast toast = Toast.makeText(SpeechActivity.this, text,
				Toast.LENGTH_SHORT);
		toast.setGravity(Gravity.TOP, 0, 500);
		toast.show();
	}

	
	
	public void setIP_Phrases() {

		Set<String> predefinedPhrases = new HashSet<String>();

		predefinedPhrases = savedPhrases.getStringSet("phrases", null);

		if (predefinedPhrases == null) {

		}

		else {

			phrases.addAll(predefinedPhrases);
			adapter.notifyDataSetChanged();

		}
		
		String valueIP = (settings.getString("ip", ""));
		addressIP = valueIP;
	}

}
