package com.example.naoworld;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ImageButton;

public class UnderConstructionActivity extends Activity {

	private ImageButton imgHome;
	
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_under_construction);
		
		imgHome = (ImageButton) findViewById(R.id.imgbtHome_Under);
	
		
		OnClickListener oclButton = new OnClickListener() {
			@Override
			public void onClick(View v) {

					startActivity(new Intent(UnderConstructionActivity.this,
							MainPanel.class));
		
			}

		};
		
		 imgHome.setOnClickListener(oclButton);

	}
	
}