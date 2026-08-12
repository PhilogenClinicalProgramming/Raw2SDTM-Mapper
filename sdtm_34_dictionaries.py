dict_cm = {}
dict_dm = {}
dict_ie = {}
dict_ex = {}
dict_vs = {}
dict_lb = {}
dict_supp = {}
dict_ae = {}
dict_ce = {}
dict_co = {}
dict_eg = {}
dict_ds = {}
dict_dv = {}
dict_pr = {}
dict_ec = {}
dict_fa = {}
dict_mh = {}
dict_mi = {}
dict_pc = {}
dict_pe = {}
dict_pp = {}
dict_rp = {}
dict_rs = {}
dict_se = {}
dict_sv = {}
dict_ta = {}
dict_te = {}
dict_ti = {}
dict_tr = {}
dict_ts = {}
dict_tu = {}
dict_tv = {}
dict_relrec = {}


dict_ce['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_ce['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_ce['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_ce['CESEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_ce['CEGRPID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_ce['CEREFID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_ce['CESPID'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_ce['CETERM'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_ce['CEDECOD'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_ce['CECAT'] = {'Source': 'Assigned' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_ce['CESCAT'] = {'Source': 'Assigned' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_ce['CEPRESP'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_ce['CEOCCUR'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_ce['CESTAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_ce['CEREASND'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_ce['CEBODSYS'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_ce['CESEV'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_ce['CETOXGR'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_ce['TAETORD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_ce['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_ce['CEDTC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_ce['CEDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 24 }
dict_ce['CEENRF'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 28 }
dict_ce['CEENRTPT'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 31 }
dict_ce['CEENTPT'] = {'Origin': 'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 32 }

dict_fa['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_fa['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_fa['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_fa['FASEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_fa['FAGRPID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_fa['FASPID'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_fa['FATESTCD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_fa['FATEST'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_fa['FAOBJ'] = {'Source': 'Assigned' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_fa['FACAT'] = {'Source': 'Assigned' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_fa['FASCAT'] = {'Source': 'Assigned' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_fa['FAORRES'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_fa['FAORRESU'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_fa['FASTRESC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_fa['FASTRESN'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_fa['FASTRESU'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_fa['FASTAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_fa['FAREASND'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_fa['FALOC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_fa['FALAT'] = {'Source': 'Investigator' ,  'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_fa['FALOBXFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_fa['FABLFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 22  }
dict_fa['FAEVAL'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 23  }
dict_fa['VISITNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_fa['VISIT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 25  }
dict_fa['VISITDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 26  }
dict_fa['TAETORD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 27  }
dict_fa['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 28  }
dict_fa['FADTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 29  }
dict_fa['FADY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 30 }


dict_mi['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_mi['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_mi['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_mi['MISEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_mi['MIGRPID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_mi['MIREFID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_mi['MISPID'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_mi['MITESTCD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_mi['MITEST'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_mi['MITSTDTL'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_mi['MICAT'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_mi['MISCAT'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_mi['MIORRES'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_mi['MIORRESU'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_mi['MISTRESC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_mi['MISTRESN'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_mi['MISTRESU'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_mi['MIRESCAT'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_mi['MISTAT'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_mi['MIREASND'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_mi['MINAM'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_mi['MISPEC'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 22  }
dict_mi['MISPCCND'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 23  }
dict_mi['MILOC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_mi['MILAT'] = {'Source': 'Investigator' ,  'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 25  }
dict_mi['MIDIR'] = {'Source': 'Investigator' ,  'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 26  }
dict_mi['MIMETHOD'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 27  }
dict_mi['MILOBXFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 28  }
dict_mi['MIBLFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 29  }
dict_mi['MIEVAL'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 30  }
dict_mi['VISITNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 31  }
dict_mi['VISIT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 32  }
dict_mi['VISITDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 33  }
dict_mi['TAETORD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 34  }
dict_mi['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 35  }
dict_mi['MIDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 36  }
dict_mi['MIDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 37 }

dict_relrec['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_relrec['RDOMAIN'] = {'Origin': 'Derived','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_relrec['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_relrec['IDVAR'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_relrec['IDVARVAL'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_relrec['RELTYPE'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_relrec['RELID'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }

dict_tv['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_tv['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_tv['VISITNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_tv['VISIT'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_tv['VISITDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_tv['ARMCD'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_tv['ARM'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_tv['TVSTRL'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_tv['TVENRL'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }

dict_tu['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_tu['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_tu['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_tu['TUSEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_tu['TUGRPID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_tu['TUREFID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_tu['TUSPID'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_tu['TULNKID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_tu['TULNKGRP'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_tu['TUTESTCD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_tu['TUTEST'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_tu['TUORRES'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_tu['TUSTRESC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_tu['TUNAM'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_tu['TULOC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_tu['TULAT'] = {'Source': 'Investigator' ,  'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_tu['TUDIR'] = {'Source': 'Investigator' ,  'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_tu['TUPORTOT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_tu['TUMETHOD'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_tu['TULOBXFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_tu['TUBLFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_tu['TUEVAL'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 22  }
dict_tu['TUEVALID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 23  }
dict_tu['TUACPTFL'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_tu['VISITNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 25  }
dict_tu['VISIT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 26  }
dict_tu['VISITDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 27  }
dict_tu['TAETORD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 28  }
dict_tu['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 29  }
dict_tu['TUDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 30  }
dict_tu['TUDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 31 }

dict_ts['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_ts['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_ts['TSSEQ'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_ts['TSGRPID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_ts['TSPARMCD'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_ts['TSPARM'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_ts['TSVAL'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_ts['TSVAL1'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_ts['TSVAL2'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_ts['TSVALNF'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_ts['TSVALCD'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_ts['TSVCDREF'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_ts['TSVCDVER'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }

dict_tr['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_tr['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_tr['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_tr['TRSEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_tr['TRGRPID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_tr['TRREFID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_tr['TRSPID'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_tr['TRLNKID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_tr['TRLNKGRP'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_tr['TRTESTCD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_tr['TRTEST'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_tr['TRORRES'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_tr['TRORRESU'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_tr['TRSTRESC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_tr['TRSTRESN'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_tr['TRSTRESU'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_tr['TRSTAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_tr['TRREASND'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_tr['TRNAM'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_tr['TRMETHOD'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_tr['TRLOBXFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_tr['TRBLFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 22  }
dict_tr['TREVAL'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 23  }
dict_tr['TREVALID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_tr['TRACPTFL'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 25  }
dict_tr['VISITNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 26  }
dict_tr['VISIT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 27  }
dict_tr['VISITDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 28  }
dict_tr['TAETORD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 29  }
dict_tr['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 30  }
dict_tr['TRDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 31  }
dict_tr['TRDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 32 }

dict_ti['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_ti['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_ti['IETESTCD'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_ti['IETEST'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_ti['IECAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_ti['IESCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_ti['TIRL'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_ti['TIVERS'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }

dict_te['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_te['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_te['ETCD'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_te['ELEMENT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_te['TESTRL'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_te['TEENRL'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_te['TEDUR'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }

dict_ta['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_ta['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_ta['ARMCD'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_ta['ARM'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_ta['TAETORD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_ta['ETCD'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_ta['ELEMENT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_ta['TABRANCH'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_ta['TATRANS'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_ta['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }

dict_sv['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_sv['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_sv['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_sv['VISITNUM'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_sv['VISIT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_sv['SVPRESP'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_sv['SVOCCUR'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_sv['SVREASOC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_sv['SVCNTMOD'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_sv['SVEPCHGI'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_sv['VISITDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_sv['SVSTDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 12 }
dict_sv['SVENDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_sv['SVSTDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_sv['SVENDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_sv['SVUPDES'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }

dict_se['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_se['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_se['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_se['SESEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_se['ETCD'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_se['ELEMENT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_se['TAETORD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_se['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_se['SESTDTC'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_se['SEENDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_se['SESTDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_se['SEENDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_se['SEUPDES'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }

dict_rs['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_rs['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_rs['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_rs['RSSEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_rs['RSGRPID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_rs['RSREFID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_rs['RSSPID'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_rs['RSLNKID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_rs['RSLNKGRP'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_rs['RSTESTCD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_rs['RSTEST'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_rs['RSCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_rs['RSSCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_rs['RSORRES'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_rs['RSORRESU'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_rs['RSSTRESC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_rs['RSSTRESN'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_rs['RSSTRESU'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_rs['RSSTAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_rs['RSREASND'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_rs['RSNAM'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_rs['RSMETHOD'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 22  }
dict_rs['RSLOBXFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 23  }
dict_rs['RSBLFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_rs['RSEVAL'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 26  }
dict_rs['RSEVALID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 27  }
dict_rs['RSACPTFL'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 28  }
dict_rs['VISITNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 29  }
dict_rs['VISIT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 30  }
dict_rs['VISITDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 31  }
dict_rs['TAETORD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 32  }
dict_rs['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 33  }
dict_rs['RSDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 34  }
dict_rs['RSDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 35 }
dict_rs['RSTPT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 36  }
dict_rs['RSTPTNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 37  }
dict_rs['RSTPTREF'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 39  }
dict_rs['RSRFTDTC'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 40  }
dict_rs['RSEVLINT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 41  }
dict_rs['RSEVINTX'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 42  }
dict_rs['RSSTRTPT'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 43  }
dict_rs['RSSTTPT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 44  }
dict_rs['RSENRTPT'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 45  }
dict_rs['RSENTPT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 46  }

dict_rp['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_rp['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_rp['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_rp['RPSEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_rp['RPGRPID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_rp['RPREFID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_rp['RPSPID'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_rp['RPTESTCD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_rp['RPTEST'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_rp['RPCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_rp['RPSCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_rp['RPORRES'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_rp['RPORRESU'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_rp['RPSTRESC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_rp['RPSTRESN'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_rp['RPSTRESU'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_rp['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 28  }
dict_rp['RPDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 30 }
dict_rp['RPDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 29  }
dict_rp['RPSTAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_rp['RPREASND'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_rp['RPLOBXFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_rp['RPBLFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 22  }
dict_rp['VISITNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_rp['VISIT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 25  }
dict_rp['RPTPT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 32  }
dict_rp['RPTPTNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 33  }
dict_rp['RPTPTREF'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 35  }
dict_rp['RPRFTDTC'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 36  }

dict_pp['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_pp['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_pp['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_pp['PPSEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_pp['PPGRPID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_pp['PPTESTCD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_pp['PPTEST'] = {'Origin':'Assigned','Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_pp['PPCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_pp['PPSCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_pp['PPORRES'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_pp['PPORRESU'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_pp['PPSTRESC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_pp['PPSTRESN'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_pp['PPSTRESU'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_pp['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_pp['PPDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 22 }
dict_pp['PPDTC'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_pp['PPSTAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_pp['PPREASND'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_pp['PPSPEC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_pp['PPANMETH'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_pp['PPTPTREF'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 23  }
dict_pp['PPRFTDTC'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_pp['PPSTINT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 25  }
dict_pp['PPENINT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 26  }

dict_pe['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_pe['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_pe['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_pe['PESEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_pe['PEGRPID'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_pe['PESPID'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_pe['PETESTCD'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_pe['PETEST'] = {'Origin':'Assigned','Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_pe['PECAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_pe['PESCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_pe['PEORRES'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_pe['PEORRESU'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_pe['PESTRESC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_pe['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 28  }
dict_pe['PEDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 30 }
dict_pe['PEDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 29  }
dict_pe['PESTAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_pe['PEREASND'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_pe['PELOC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_pe['PELAT'] = {'Origin':'Derived','Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_pe['PEMETHOD'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_pe['PELOBXFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_pe['PEBLFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 22  }
dict_pe['VISITNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_pe['VISIT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 25  }
dict_pe['PETPT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 31  }
dict_pe['PESTATOTH'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 32  }
dict_pe['PECLSIG'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 33  }

dict_pc['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_pc['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_pc['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_pc['PCSEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_pc['PCSPID'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_pc['PCTESTCD'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_pc['PCTEST'] = {'Origin':'Assigned','Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_pc['PCCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_pc['PCSCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_pc['PCORRES'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_pc['PCORRESU'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_pc['PCSTRESC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_pc['PCSTRESN'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_pc['PCSTRESU'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_pc['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 31  }
dict_pc['PCDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 34 }
dict_pc['PCDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 32  }
dict_pc['PCSTAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_pc['PCREASND'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_pc['PCNAM'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_pc['PCSPEC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_pc['PCSPCCND'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_pc['PCMETHOD'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 22  }
dict_pc['PCLLOQ'] = {'Origin': 'Laboratory Manual','Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 25  }
dict_pc['VISITNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 27  }
dict_pc['VISIT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 28  }
dict_pc['PCTPT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 36  }
dict_pc['PCTPTNUM'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 37  }
dict_pc['PCTPTREF'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 40  }
dict_pc['PCRFTDTC'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 39  }
dict_pc['PCELTM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 38  }
dict_pc['PCEVLINT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 41  }
dict_pc['PCTPTSTAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 42  }

dict_mh['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_mh['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_mh['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_mh['MHSEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_mh['MHGRPID'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_mh['MHREFID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_mh['MHSPID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_mh['MHTERM'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_mh['MHLLT'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_mh['MHDECOD'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_mh['MHEVDTYP'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_mh['MHCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_mh['MHSCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_mh['MHPRESP'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_mh['MHOCCUR'] = {'Origin':'Assigned','Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_mh['MHSTAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_mh['MHREASND'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_mh['MHBODSYS'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_mh['MHSOC'] = {'Origin':'Assigned','Source': 'Vendor', 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_mh['TAETORD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_mh['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_mh['MHDTC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 22  }
dict_mh['MHSTDTC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 23  }
dict_mh['MHENDTC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_mh['MHDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 25 }
dict_mh['MHENRF'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 26 }
dict_mh['MHENRTPT'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 27 }
dict_mh['MHENTPT'] = {'Origin': 'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 28 }
dict_mh['MHTOXGR'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 29 }
dict_mh['MHTOXGRYN'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 30 }
dict_mh['MHPREV'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 31 }

dict_ec['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_ec['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_ec['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_ec['ECSEQ'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_ec['ECTRT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_ec['ECMOOD'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_ec['ECPRESP'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_ec['ECOCCUR'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_ec['ECREASOC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_ec['ECDOSE'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_ec['ECDOSTXT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_ec['ECDOSU'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_ec['ECDOSFRQ'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_ec['ECDOSFRM'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_ec['ECDOSTOT'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 22  }
dict_ec['ECDOSRGM'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 23  }
dict_ec['ECROUTE'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_ec['ECLOT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 25  }
dict_ec['ECLOC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 26  }
dict_ec['ECLAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 27  }
dict_ec['ECDIR'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 28  }
dict_ec['ECPORTOT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 29  }
dict_ec['ECPSTRG'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 31  }
dict_ec['ECPSTRGU'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 32  }
dict_ec['ECADJ'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 33  }
dict_ec['ECSTDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 36  }
dict_ec['ECENDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 37  }
dict_ec['EPOCH'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 35  }
dict_ec['ECSTDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 38  }
dict_ec['ECENDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 39  }
dict_ec['ECTPT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 41  }
dict_ec['ECTPTNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 42  }
dict_ec['ECRFTDTC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 45  }

dict_pr['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_pr['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_pr['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_pr['PRSEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_pr['PRGRPID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_pr['PRSPID'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_pr['PRLNKID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_pr['PRLNKGRP'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_pr['PRTRT'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_pr['PRDECOD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_pr['PRCAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_pr['PRSCAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_pr['PRPRESP'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_pr['PROCCUR'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_pr['PRINDC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_pr['PRDOSE'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_pr['PRDOSTXT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_pr['PRDOSU'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_pr['PRDOSFRM'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_pr['PRDOSFRQ'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_pr['PRDOSRGM'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_pr['PRROUTE'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 22  }
dict_pr['PRLOC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 23  }
dict_pr['PRLAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_pr['PRDIR'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 25  }
dict_pr['PRPORTOT'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 26  }
dict_pr['VISITNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 27  }
dict_pr['VISIT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 28  }
dict_pr['VISITDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 29  }
dict_pr['TAETORD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 30  }
dict_pr['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 31  }
dict_pr['PRSTDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 32  }
dict_pr['PRENDTC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 33  }
dict_pr['PRSTDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 34  }
dict_pr['PRENDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 35  }
dict_pr['PRTPT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 37  }
dict_pr['PRTPTNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 38  }
dict_pr['PRELTM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 39  }
dict_pr['PRTPTREF'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 40  }
dict_pr['PRRFTDTC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 41  }
dict_pr['PRSTRTPT'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 42  }
dict_pr['PRSTTPT'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 43  }
dict_pr['PRENRTPT'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 44  }
dict_pr['PRENTPT'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 45  }
dict_pr['PRLATOTH'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 46  }
dict_pr['PRNUF'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 47  }

dict_dv['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_dv['DOMAIN'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_dv['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_dv['DVSEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_dv['DVREFID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_dv['DVSPID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_dv['DVTERM'] = {'Origin':'Derived','Source': 'Sponsor', 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_dv['DVDECOD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_dv['DVCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_dv['DVSCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_dv['TAETORD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_dv['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_dv['DVSTDTC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_dv['DVENDTC'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_dv['DVSTDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_dv['DVENDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }

dict_ds['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_ds['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_ds['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_ds['DSSEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_ds['DSGRPID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_ds['DSREFID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_ds['DSSPID'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_ds['DSTERM'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_ds['DSDECOD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_ds['DSCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_ds['DSSCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_ds['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_ds['DSDTC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_ds['DSSTDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_ds['DSDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_ds['DSSTDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_ds['DSPERIOD'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 17  }
dict_ds['DSTERMOTH'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 18  }
dict_ds['DSOTH'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 19  }
dict_ds['DSDECODOTH'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 19  }

dict_eg['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_eg['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_eg['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_eg['EGSEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_eg['EGGRPID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_eg['EGSPID'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_eg['EGTESTCD'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_eg['EGTEST'] = {'Origin':'Assigned','Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_eg['EGCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_eg['EGSCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_eg['EGPOS'] = {'Origin':'Assigned','Source': 'Protocol' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_eg['EGORRES'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_eg['EGORRESU'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_eg['EGSTRESC'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_eg['EGSTRESN'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_eg['EGSTRESU'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_eg['EGSTAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_eg['EGREASND'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_eg['EGMETHOD'] = {'Origin':'Assigned','Source': 'Protocol' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_eg['EGLOBXFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 26  }
dict_eg['EGBLFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 27  }
dict_eg['EGCLSIG'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 31  }
dict_eg['VISITNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 33  }
dict_eg['VISIT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 34  }
dict_eg['VISITDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 35  }
dict_eg['TAETORD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 36  }
dict_eg['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 37  }
dict_eg['EGDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 38  }
dict_eg['EGDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 39  }
dict_eg['EGTPT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 40  }
dict_eg['EGTPTNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 41  }
dict_eg['EGTPTREF'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 43  }
dict_eg['EGRFTDTC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 44  }
dict_eg['EGTESTSTAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 45  }
dict_eg['EGTESTREASND'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 46  }
dict_eg['EGTESTCS'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 47  }
dict_eg['EGTESTORRES'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 48  }

dict_co['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_co['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_co['RDOMAIN'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_co['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_co['COSEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_co['IDVAR'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_co['IDVARVAL'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_co['COREF'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_co['COVAL'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_co['COVAL1'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_co['COVAL2'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_co['COEVAL'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_co['COEVALID'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_co['CODTC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_co['CODY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }

dict_ae['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_ae['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_ae['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_ae['AESEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_ae['AEGRPID'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_ae['AEREFID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_ae['AESPID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_ae['AETERM'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_ae['AELLT'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_ae['AELLTCD'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_ae['AEDECOD'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_ae['AEPTCD'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_ae['AEHLT'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_ae['AEHLTCD'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_ae['AEHLGT'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_ae['AEHLGTCD'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_ae['AECAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_ae['AESCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_ae['AEPRESP'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_ae['AEBODSYS'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 22  }
dict_ae['AEBDSYCD'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 23  }
dict_ae['AESOC'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_ae['AESOCCD'] = {'Origin':'Assigned','Source': 'Vendor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 25  }
dict_ae['AELOC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 26  }
dict_ae['AESEV'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 27  }
dict_ae['AESER'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 28  }
dict_ae['AEACN'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 29  }
dict_ae['AEACNOTH'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 30  }
dict_ae['AEREL'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 32  }
dict_ae['AERELNST'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 34  }
dict_ae['AEPATT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 35  }
dict_ae['AEOUT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 36  }
dict_ae['AESCONG'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 38  }
dict_ae['AESDISAB'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 39  }
dict_ae['AESDTH'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 40  }
dict_ae['AESHOSP'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 41  }
dict_ae['AESLIFE'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 42  }
dict_ae['AESMIE'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 44  }
dict_ae['AERLPRT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 47  }
dict_ae['AECONTRT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 49  }
dict_ae['AETOXGR'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 50  }
dict_ae['TAETORD'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 51  }
dict_ae['AESTDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 53  }
dict_ae['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 52  }
dict_ae['AEENDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 54  }
dict_ae['AESTDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 55 }
dict_ae['AEENDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 56 }
dict_ae['AEENRF'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 58 }
dict_ae['AEENRTPT'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 59 }
dict_ae['AEENTPT'] = {'Origin': 'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 60 }
dict_ae['AEFUPFL'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 61 }
dict_ae['AEBLFL'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 62 }
dict_ae['AEPATTOTH'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 63 }
dict_ae['AEFUPTYP'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 64 }
dict_ae['AEEXP'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 65 }
dict_ae['AEPREV'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 66 }
dict_ae['AESERCRT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 67 }
dict_ae['AENEC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 68 }
dict_ae['AECONTRTOTH'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 69 }


dict_supp['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_supp['RDOMAIN'] = {'Origin': 'Derived','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_supp['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_supp['IDVAR'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_supp['IDVARVAL'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_supp['QNAM'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_supp['QLABEL'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_supp['QVAL'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_supp['QORIG'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_supp['QEVAL'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }

dict_lb['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_lb['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_lb['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_lb['LBSEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_lb['LBTESTCD'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_lb['LBTEST'] = {'Origin':'Assigned','Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_lb['LBCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_lb['LBORRES'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_lb['LBORRESU'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_lb['LBRESSCL'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_lb['LBORNRLO'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_lb['LBORNRHI'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_lb['LBSTNRLO'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 26  }
dict_lb['LBSTNRHI'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 27  }
dict_lb['LBSTRESC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 23  }
dict_lb['LBNRIND'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 29  }
dict_lb['LBDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 52  }
dict_lb['LBSTRESN'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_lb['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 51  }
dict_lb['LBDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 54 }
dict_lb['LBSTRESU'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 25  }
dict_lb['LBSTAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 30  }
dict_lb['LBREASND'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 31  }
dict_lb['LBNAM'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 32  }
dict_lb['LBSPEC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 33  }
dict_lb['LBLOBXFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 40  }
dict_lb['LBBLFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 41  }
dict_lb['LBTOX'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 44  }
dict_lb['LBTOXGR'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 45  }
dict_lb['LBCLSIG'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 46  }
dict_lb['VISITNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 47  }
dict_lb['VISIT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 48  }
dict_lb['LBTPT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 56  }
dict_lb['LBTPTNUM'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 57  }
dict_lb['LBORRESUOTH'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 63  }

dict_vs['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_vs['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_vs['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_vs['VSSEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_vs['VSTESTCD'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_vs['VSTEST'] = {'Origin':'Assigned','Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_vs['VSCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 9  }
dict_vs['VSSCAT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_vs['VSPOS'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_vs['VSORRES'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_vs['VSORRESU'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_vs['VSSTRESC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_vs['VSDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 32  }
dict_vs['VSSTRESN'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_vs['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 31  }
dict_vs['VSDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 33 }
dict_vs['VSSTRESU'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_vs['VSSTAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_vs['VSREASND'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_vs['VSBLFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 22  }
dict_vs['VSLOBXFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_vs['VSTOX'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_vs['VSTOXGR'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 25  }
dict_vs['VSCLSIG'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 26  }
dict_vs['VISITNUM'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 27  }
dict_vs['VISIT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 28  }
dict_vs['VSTPT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 34  }
dict_vs['VSTPTNUM'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 35  }
dict_vs['VSTPTREF'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 37  }
dict_vs['VSRFTDTC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 38  }
dict_vs['VSNRIND'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }

dict_ex['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_ex['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_ex['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_ex['EXSEQ'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_ex['EXTRT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_ex['EXDOSE'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_ex['EXDOSTXT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_ex['EXDOSU'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_ex['EXDOSFRQ'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_ex['EXDOSFRM'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_ex['EXDOSRGM'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_ex['EXROUTE'] = {'Origin':'Protocol','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_ex['EXLOT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 20  }
dict_ex['EXLOC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_ex['EXLAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 22  }
dict_ex['EXDIR'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 23  }
dict_ex['EXADJ'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 25  }
dict_ex['EXSTDTC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 28  }
dict_ex['EXENDTC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 29  }
dict_ex['EPOCH'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 27  }
dict_ex['EXSTDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 30  }
dict_ex['EXENDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 31  }
dict_ex['EXVAMT'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 38  }
dict_ex['EXPRELOT'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 39  }
dict_ex['EXFULLDOSEYN'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 40  }
dict_ex['EXREMDOSE'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 41  }

dict_cm['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_cm['DOMAIN'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_cm['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_cm['CMSEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_cm['CMSPID'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_cm['CMTRT'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_cm['CMMODIFY'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_cm['CMCAT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_cm['CMINDC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_cm['CMDOSE'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_cm['CMDOSU'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_cm['CMDOSFRQ'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 23  }
dict_cm['CMDOSTOT'] = {'Origin':'Derived', 'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_cm['CMSTDY'] = {'Origin':'Derived', 'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 33  }
dict_cm['CMENDY'] = {'Origin':'Derived', 'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 34  }
dict_cm['CMROUTE'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 26  }
dict_cm['EPOCH'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 30  }
dict_cm['CMSTDTC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 31  }
dict_cm['CMENDTC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 32  }
dict_cm['CMENRF'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 37  }
dict_cm['CMENRTPT'] = {'Origin': 'Derived' ,'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 40  }
dict_cm['CMENTPT'] = {'Origin': 'Assigned' ,'Source': 'Investigator', 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 41  }
dict_cm['CMINGRD'] = {'Source': 'Investigator' , 'Core':'',
                         'Variable Type': 'SUPP', 'Variable Order': 42  }
dict_cm['CMAENO'] = {'Source': 'Investigator' , 'Core':'',
                         'Variable Type': 'SUPP', 'Variable Order': 43  }
dict_cm['CMMHNO'] = {'Source': 'Investigator' , 'Core':'',
                         'Variable Type': 'SUPP', 'Variable Order': 44  }
dict_cm['CMINDOTH'] = {'Source': 'Investigator' , 'Core':'',
                         'Variable Type': 'SUPP', 'Variable Order': 45  }
dict_cm['CMROUTEOTH'] = {'Source': 'Investigator' , 'Core':'',
                         'Variable Type': 'SUPP', 'Variable Order': 46  }
dict_cm['CMLINE'] = {'Source': 'Investigator' , 'Core':'',
                         'Variable Type': 'SUPP', 'Variable Order': 47  }
dict_cm['CMCYCL'] = {'Source': 'Investigator' , 'Core':'',
                         'Variable Type': 'SUPP', 'Variable Order': 48  }
dict_cm['CMCYCLIND'] = {'Source': 'Investigator' , 'Core':'',
                         'Variable Type': 'SUPP', 'Variable Order': 49  }
dict_cm['CMADJTRT'] = {'Source': 'Investigator' , 'Core':'',
                         'Variable Type': 'SUPP', 'Variable Order': 50  }
dict_cm['CMPREV'] = {'Source': 'Investigator' , 'Core':'',
                         'Variable Type': 'SUPP', 'Variable Order': 51  }


dict_dm['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_dm['DOMAIN'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_dm['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_dm['ACTARM'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 27  }
dict_dm['ACTARMCD'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 26  }
dict_dm['ACTARMUD'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 29  }
dict_dm['ARMNRS'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 28  }
dict_dm['AGE'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 19  }
dict_dm['AGEU'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_dm['ARM'] = {'Origin': 'Assigned','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 25  }
dict_dm['ARMCD'] = {'Origin': 'Assigned', 'Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 24  }
dict_dm['BRTHDTC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_dm['COUNTRY'] = {'Origin': 'Assigned', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 30  }
dict_dm['DMDTC'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 31  }
dict_dm['DMDY'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 32  }
dict_dm['DTHDTC'] = {'Origin':'Collected','Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_dm['DTHFL'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 14  }
dict_dm['ETHNIC'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 23  }
dict_dm['RACE'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 22  }
dict_dm['RFPENDTC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_dm['RFENDTC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_dm['RFICDTC'] = {'Source': 'Investigator' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_dm['RFSTDTC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_dm['RFXSTDTC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_dm['RFXENDTC'] = {'Origin':'Derived','Source': 'Sponsor' , 'Core':'Exp',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_dm['SEX'] = {'Source': 'Investigator' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 21  }
dict_dm['SITEID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 15  }
dict_dm['INVNAM'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_dm['SUBJID'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_dm['DMCOHORT'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'',
                         'Variable Type': 'SUPP', 'Variable Order': 33  }

dict_ie['STUDYID'] = {'Origin':'Protocol', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 1  }
dict_ie['DOMAIN'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 2  }
dict_ie['USUBJID'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 3  }
dict_ie['EPOCH'] = {'Origin':'Assigned', 'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 16  }
dict_ie['IECAT'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 8  }
dict_ie['IEORRES'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 10  }
dict_ie['IESEQ'] = {'Origin':'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 4  }
dict_ie['IESPID'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 5  }
dict_ie['IESTRESC'] = {'Origin': 'Derived', 'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 11  }
dict_ie['IETEST'] = {'Origin':'Assigned','Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 7  }
dict_ie['IETESTCD'] = {'Source': 'Sponsor' , 'Core':'Req',
                         'Variable Type': 'SDTM', 'Variable Order': 6  }
dict_ie['VISIT'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 13  }
dict_ie['VISITNUM'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 12  }
dict_ie['IEDTC'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 17  }
dict_ie['IEDY'] = {'Source': 'Sponsor' , 'Core':'Perm',
                         'Variable Type': 'SDTM', 'Variable Order': 18  }
dict_ie['IECREATCLR'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 19  }
dict_ie['IESCR'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 20  }
dict_ie['IESCRU'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 21  }
dict_ie['IESCRUOTH'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 22  }
dict_ie['IEYN'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 23  }
dict_ie['IEENROLYN'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 24  }
dict_ie['IECOHORT'] = {'Source': 'Investigator' , 'Core':'Perm',
                         'Variable Type': 'SUPP', 'Variable Order': 25  }
