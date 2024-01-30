#input that takes in a string --> compares string to array --> gives list of what vehicles to expect

import json


Rank1_USAG = {"M2A4 BR: Reserve", "M2 BR: 1.3" , "LVT(A)(1) BR: Reserve", "M13 MGMC BR: 1.7"}
Rank2_USAG = {}
Rank3_USAG = {}
Rank4_USAG = {}
Rank5_USAG = {}
Rank6_USAG = {}
Rank7_USAG = {}

Rank1_GERG = {}
Rank2_GERG = {}
Rank3_GERG = {}
Rank4_GERG = {}
Rank5_GERG = {}
Rank6_GERG = {}
Rank7_GERG = {}

Rank1_RUSG = {}
Rank2_RUSG = {}
Rank3_RUSG = {}
Rank4_RUSG = {}
Rank5_RUSG = {}
Rank6_RUSG = {}
Rank7_RUSG = {}

Rank1_GBG = {}
Rank2_GBG = {}
Rank3_GBG = {}
Rank4_GBG = {}
Rank5_GBG = {}
Rank6_GBG = {}
Rank7_GBG = {}

Rank1_ITAG = {}
Rank2_ITAG = {}
Rank3_ITAG = {}
Rank4_ITAG = {}
Rank5_ITAG = {}
Rank6_ITAG = {}
Rank7_ITAG = {}

Rank1_FRAG = {}
Rank2_FRAG = {}
Rank3_FRAG = {}
Rank4_FRAG = {}
Rank5_FRAG = {}
Rank6_FRAG = {}
Rank7_FRAG = {}

Rank1_SWEG = {}
Rank2_SWEG = {}
Rank3_SWEG = {}
Rank4_SWEG = {}
Rank5_SWEG = {}
Rank6_SWEG = {}
Rank7_SWEG = {}

Rank1_ISRG = {}
Rank2_ISRG = {}
Rank3_ISRG = {}
Rank4_ISRG = {}
Rank5_ISRG = {}
Rank6_ISRG = {}
Rank7_ISRG = {}

SWE = {Rank1_SWEG, Rank2_SWEG, Rank3_SWEG, Rank4_SWEG, Rank5_SWEG, Rank6_SWEG, Rank7_SWEG};
FRA = {Rank1_FRAG, Rank2_FRAG, Rank3_FRAG, Rank4_FRAG, Rank5_FRAG, Rank6_FRAG, Rank7_FRAG};
ISR = {Rank1_ISRG, Rank2_ISRG, Rank3_ISRG, Rank4_ISRG, Rank5_ISRG, Rank6_ISRG, Rank7_ISRG};
ITA = {Rank1_ITAG, Rank2_ITAG, Rank3_ITAG, Rank4_ITAG, Rank5_ITAG, Rank6_ITAG, Rank7_ITAG};
GB = {Rank1_GBG, Rank2_GBG, Rank3_GBG, Rank4_GBG, Rank5_GBG, Rank6_GBG, Rank7_GBG};
RUS = {Rank1_RUSG, Rank2_RUSG, Rank3_RUSG, Rank4_RUSG, Rank5_RUSG, Rank6_RUSG, Rank7_RUSG};
GER = {Rank1_GERG, Rank2_GERG, Rank3_GERG, Rank4_GERG, Rank5_GERG, Rank6_GERG, Rank7_GERG};
USA = {Rank1_USAG, Rank2_USAG, Rank3_USAG, Rank4_USAG, Rank5_USAG, Rank6_USAG, Rank7_USAG};

Nations = {USA,GER,RUS,GB,ITA,ISR,FRA,SWE};

USA_json = json.dumps(USA)
GER_json = json.dumps(GER)
RUS_json = json.dumps(RUS)
GB_json = json.dumps(GB)
ITA_json = json.dumps(ITA)
ISR_json = json.dumps(ISR)
FRA_json = json.dumps(FRA)
SWE_json = json.dumps(SWE)


#What tank are you in --> user input --> outputs what other tanks are in that br range of (1.0 Lower -- Your BR -- 1.0 Higher)

User_Tank = input('What tank are you in ?\n')
if User_Tank in Nation




print(User_Tank)