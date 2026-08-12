import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB

def compute_traindf(module,crf_type,teststudy):
    if crf_type == 'PheedIt':
        full_test_data_path=os.path.join('Temporary_Folder',crf_type,'test_data','Final')
    else:
        full_test_data_path=os.path.join('Temporary_Folder',crf_type,'test_data')
    train_files = os.listdir(full_test_data_path)

    train_df = pd.DataFrame()
    for f in train_files:
        if f.startswith(module) and teststudy not in f:
            if module == 'mh':
                if 'mhd' not in f:
                    df = pd.read_csv(os.path.join(full_test_data_path,f),sep=';')
                    train_df = pd.concat([train_df,df])
            else:
                df = pd.read_csv(os.path.join(full_test_data_path,f),sep=';')
                train_df = pd.concat([train_df,df])
    train_df.to_csv('full_train_'+module+'.csv',sep=';')

    unique_train_df = train_df.drop_duplicates()
    unique_train_df = unique_train_df.dropna()
    unique_train_df['ID'] = unique_train_df['ID'].str.strip(' ')
    unique_train_df['label'] = unique_train_df.apply(lambda row: row['text'].replace(row['ID'], ''), axis=1)
    
    return unique_train_df

def build_NLPmodel(df,seed=2):
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
    X = vectorizer.fit_transform(df['ID'])
    X_train_test, X_test_test, y_train_test, y_test_test = train_test_split(X, df['sdtm'], test_size=0.1, random_state=seed)
    classifier = SVC(kernel='linear',random_state=42)
    classifier.fit(X_train_test, y_train_test)
    y_pred = classifier.predict(X_test_test)
    check = pd.DataFrame(vectorizer.inverse_transform(X_test_test))
    check['pred']=y_pred
    accuracy = accuracy_score(y_test_test, y_pred)
    report = classification_report(y_test_test, y_pred)#, target_names=newsgroups.target_names)
    classifier = SVC(kernel='linear',random_state=42)
    classifier.fit(X, df['sdtm'])
    
    return check,vectorizer,classifier,accuracy,report

def computeWeights(df,scale='off'):
    weights = {}
    for i in df['sdtm']:
        if scale == 'off':
            weights[i]=1
        else:
            if i == "DROP":
                weights[i] = 0.2
            else:
                weights[i] = 2
                
    return weights

def build_NLPmodelWeights(df,weights):
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
    X = vectorizer.fit_transform(df['ID'])
    X_train_test, X_test_test, y_train_test, y_test_test = train_test_split(X, df['sdtm'], test_size=0.1, random_state=2)
    classifier = SVC(kernel='linear',random_state=42, class_weight=weights)
    classifier.fit(X_train_test, y_train_test)
    y_pred = classifier.predict(X_test_test)
    check = pd.DataFrame(vectorizer.inverse_transform(X_test_test))
    check['pred']=y_pred
    classifier = SVC(kernel='linear',random_state=42, class_weight=weights)
    classifier.fit(X, df['sdtm'])
    
    return check,vectorizer,classifier

def build_NLPmodelWeightsPheedIt(df,weights):
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
    X = vectorizer.fit_transform(df['label'])
    X_train_test, X_test_test, y_train_test, y_test_test = train_test_split(X, df['sdtm'], test_size=0.1, random_state=2)
    classifier = SVC(kernel='linear',random_state=42, class_weight=weights)
    classifier.fit(X_train_test, y_train_test)
    y_pred = classifier.predict(X_test_test)
    check = pd.DataFrame(vectorizer.inverse_transform(X_test_test))
    check['pred']=y_pred
    classifier = SVC(kernel='linear',random_state=42, class_weight=weights)
    classifier.fit(X, df['sdtm'])
    
    return check,vectorizer,classifier

def check_teststudy(out):
    metrics_df = pd.DataFrame([[None, None, None, None, None, None, None]], columns=['tp','fn','fp','tn','recall', 'specificity', 'accuracy'])
    right_ass = out[out.pred.str.strip(' ') == out.real.str.strip(' ')].shape[0]
    total = out.shape[0]
    
    accuracy = right_ass/total
    
    tp = out[((out.real.str.strip(' ') != 'DROP') & (out.pred.str.strip(' ') != 'DROP')) ].shape[0]
    tn = out[((out.real.str.strip(' ') == 'DROP') & (out.pred.str.strip(' ') == 'DROP')) ].shape[0]
    fn = out[((out.real.str.strip(' ') != 'DROP') & (out.pred.str.strip(' ') == 'DROP')) ].shape[0]
    fp = out[((out.real.str.strip(' ') == 'DROP') & (out.pred.str.strip(' ') != 'DROP')) ].shape[0]
    
    metrics_df['recall'] = tp/(tp+fn)
    metrics_df['specificity'] = tn/(tn+fp)
    metrics_df['tp'] = tp
    metrics_df['tn'] = tn
    metrics_df['fp'] = fp
    metrics_df['fn'] = fn
    metrics_df['accuracy'] = accuracy

    metrics_df['f1'] = 2 * ( ((tn/(tn+fp))) * (tp/(tp+fn)) ) / ( ((tn/(tn+fp))) + (tp/(tp+fn)) )
    
    return metrics_df

def predict_annot(module,study,code,path,outpath,vectorizer,classifier):
    train_files = os.listdir(path)
    listmod = []
    for f in train_files:
        if f.startswith(module) and study in f:
            df_mod = pd.read_csv(os.path.join(path,f),sep=';')
            listmod.append(df_mod)
    if len(listmod) > 1:
        df_tot = pd.concat(listmod, ignore_index=True)
    else:
        df_tot = listmod[0] 
    X = vectorizer.transform(df_tot['ID'])
    y = classifier.predict(X)
    out = pd.DataFrame(vectorizer.inverse_transform(X))
    out['pred']=y
    out2 = out[out.pred!='DROP']
    out2[0]=out2[0].str.upper()
    out2['pred'] = out['pred'].str.strip(' ')
    out2.to_csv(os.path.join(outpath,module+"_annotation_"+code+".csv"),sep=';')
    out['real'] = df_tot['sdtm']

    return out

def predict_annotPheedIt(module,study,code,path,outpath,vectorizer,classifier):
    train_files = os.listdir(path)
    listmod = []
    for f in train_files:
        if f.startswith(module) and study in f:
            df_mod = pd.read_csv(os.path.join(path,f),sep=';')
            listmod.append(df_mod)
    if len(listmod) > 1:
        df_tot = pd.concat(listmod, ignore_index=True)
    else:
        df_tot = listmod[0] 

    df_tot['label'] = df_tot.apply(lambda row: row['text'].replace(row['ID'], ''), axis=1)
    X = vectorizer.transform(df_tot['label'])
    y = classifier.predict(X)
    out = pd.DataFrame(vectorizer.inverse_transform(X))
    out['pred']=y
    out2 = out[out.pred!='DROP']
    out2[0]=out2[0].str.upper()
    out2['pred'] = out['pred'].str.strip(' ')
    out2.to_csv(os.path.join(outpath,module+"_annotation_"+code+".csv"),sep=';')
    out['real'] = df_tot['sdtm']

    return out