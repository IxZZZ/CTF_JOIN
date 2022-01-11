#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <bits/stdc++.h>

using namespace std;

char v6[0x1F4];

string character = 	"ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff3"
					"00305878012345623010341238012344121153455678012327627513245678033"
					"56468145234567423634656801234567801234567801234567801234567801234"
					"56780123456780123456780123456780123456780123456780123456780124857"
					"7878274567801215767600234567086284567Good Job!x"
					"Try Againx"
					"y"
					"23423122422123423122422123342331232423212434243124242421243424312"
					"42424212433424331243242432123423122422123423122422123342331232423"
					"21343124213431242133433132432143443142442143443142442143344331432"
					"443213431242134312421334331324321x"
					"44244442444432443442444452445412414124141324134124141524151421414"
					"21414321431421414521451121111211113211311211115211522422124212424"
					"24212442412242212421252425212542512542425421254425412524252125425"
					"12242212421242424212442412242212421242141424421444124214152452154"
					"51542454215445415245215451242141424421444124214122426264662242626"
					"46632324326326334363622426264662242626466323243263263343636323243"
					"26326334363632324326326334363633233243326332633334336336x"
					"y"
					"34333534434334534333534434334534443443344534434334534333534434334"
					"53433352423252442432452423252442432452444244324452442432452423252"
					"44243245242325x"
					"42442444244234234423425425442544444444343443454544512412441241231"
					"2341231251254125141441413134131515415x"
					"y"
					"34334234433442346334623463346231331231433142316331623163316224324"
					"22443244224632462246324622132122143214221632162216321625343534253"
					"44353442534635346253463534625313531253143531425316353162531635316"
					"25243524252443524425246352462524635246252135212521435214252163521"
					"62521635216234334234433442346334623463346231331231433142316331623"
					"16331622432422443244224632462246324622132122143214221632162216321"
					"62x"
					"44424444412441434243443124314542454451245144424444412441434243443"
					"12431454245445124514344243444341243414334243344331243314354243544"
					"35124351344234434123413342334331233135423543512351344234434123413"
					"34233433123313542354351235133442334433412334133342333433312333133"
					"54233543351233515442544541254153425345312531554255455125515442544"
					"54125415342534531253155425545512551534425344534125341533425334533"
					"125331535425354535125351x";


void sub0() {
	if (fork() || !fork()) {
		wait(0);
	} else {
		wait(0);
		v6[strlen(v6)] = '5';
		cout << '5';
	}
}

void sub1() {
	if (fork()) {
		wait(0);
		v6[strlen(v6)] = '1';
		cout << '1';
	} else {
		v6[strlen(v6)] = '4';
		cout << '4';
	}
}

void sub2() {
	if (fork()) {
		wait(0);
		v6[strlen(v6)] = '2';
		cout << '2';
	} else {
		v6[strlen(v6)] = '3';
		cout << '3';
	}
}

void sub3() {
	if (fork()) {
		wait(0);
		if (fork()) {
			wait(0);
			if (fork()) {
				wait(0);
				if (fork()) {
					wait(0);
					v6[strlen(v6)] = '5';
					cout << '5';
				}
			} else {
				v6[strlen(v6)] = '3';
				cout << '3';
			}
		}		
	}
}

void sub4() {
	if (fork()) {
		wait(0);
		if (fork()) {
			wait(0);
		} else {
			v6[strlen(v6)] = '4';
			cout << '4';
		}
	}
}

void sub5() {
	if (fork()) {
		wait(0);
		if (fork()) {
			wait(0);
			v6[strlen(v6)] = '5';
			cout << '5';
		} else {
			v6[strlen(v6)] = '3';
			cout << '3';
		}
	} else {
		v6[strlen(v6)] = '4';
		cout << '4';
	}
}

void sub6() {
	if (fork()) {
		wait(0);
		if (fork() || fork()) {
			wait(0);
			wait(0);
			v6[strlen(v6)] = '6';
			cout << '6';
		} else {
			v6[strlen(v6)] = '4';
			cout << '4';
		}
	}
}

void sub7() {
	if (fork()) {
		wait(0);
		if (fork()) {
			wait(0);
			v6[strlen(v6)] = '3';
			cout << '3';
		}
	}
}

void sub8() {
	if (fork()) {
		wait(0);
	} else {
		v6[strlen(v6)] = '2';
		cout << '2';
	}
}

bool test(string flag, const string& teststring) {
	int v4 = getpid();
	
	for (int i = 0; i < 0x1F4; i++) {
		v6[i] = 0;
	}
	
	//flag = "8";

	for (int i = 0; i < (int)flag.size(); i++) {
		if (flag[i] == '0') {
			sub0();
		} else if (flag[i] == '1') {
			sub1();
		} else if (flag[i] == '2') {
			sub2();
		} else if (flag[i] == '3') {
			sub3();
		} else if (flag[i] == '4') {
			sub4();
		} else if (flag[i] == '5') {
			sub5();
		} else if (flag[i] == '6') {
			sub6();
		} else if (flag[i] == '7') {
			sub7();
		} else if (flag[i] == '8') {
			sub8();
		} else {
			continue;
		}
	}

	if (v4 != getpid()) {
    	exit(0);
	}
	

	if ( flag == "84721") {
		for (int i = 0; i < 20; i++) {
			//cout << (int)v6[i] << '\n';
		}
	}	

	for (int i = 0; i < (int)teststring.size(); i++) {
		if (v6[i] != teststring[i]) {
			return false;
		}
	}

	return true;

}

int c(char a) {
	int i = 1;
	int ans = 0;
	while (a) {
		int b = a % 10;
		a /= 10;
		ans += b * i;
		i *= 16;
	}
	return ans;
}


void bruteforce(const vector<string>& mod, string flag, int* require, const string& teststring) {
	if (flag.size() == 5) {
		//cout << "Try: " << flag << '\n';
		string real_test = "";		
		for (int i = 0; i < 5; i++) {
			real_test += character[c(flag[i])];
		}
		test(real_test, teststring);
		cout << flag << '\n';
		//if (test(real_test, teststring) || flag == "i_to9") {
			//cout << real_test << '\n';
			//return;
		//} 
	}
	else {
		for (int i = 0; i < (int)mod[require[flag.size()]].size(); i++) {
			bruteforce(mod, flag + mod[require[flag.size()]][i], require, teststring);
		}
	}
}

int main() {
			
	vector<string> mod(9);

	mod[0] = "$-6?HQZclu~";
	mod[1] = "%.7@IR[dmv";
	mod[2] = "&/8AJS\\enw";
	mod[3] = "'09BKT]fox";
	mod[4] = "(1:CLU^gpy";
	mod[5] = ")2;DMV_hqz";
	mod[6] = "!*3<ENW`ir{";
	mod[7] = "\"+4=FOXajs|";
	mod[8] = "#,5>GPYbkt}";

	string teststring = "234231224221234231224221233423312324232124342431242424212434243124242421243342433124324243212342312242212342312242212334233123242321343124213431242133433132432143443142442143443142442143344331432443213431242134312421334331324321";

	int reg[] = {6, 5, 8, 3, 3};

	string flag = "";

	bruteforce(mod, flag, reg, teststring);
	
	//cout << test("84721", teststring);
	
	//cout << "\nTest done";

	return 0;

}
