{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'numpy'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[2], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mnumpy\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mnp\u001b[39;00m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'numpy'"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pd' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[4], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m data_thyao_dortsaat \u001b[38;5;241m=\u001b[39m \u001b[43mpd\u001b[49m\u001b[38;5;241m.\u001b[39mread_excel(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mTHYAO_240Dk.xlsx\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m      2\u001b[0m data_thyao_dortsaat\n",
      "\u001b[0;31mNameError\u001b[0m: name 'pd' is not defined"
     ]
    }
   ],
   "source": [
    "data_thyao_dortsaat = pd.read_excel('THYAO_240Dk.xlsx')\n",
    "data_thyao_dortsaat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'data_thyao_dortsaat' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[5], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mdata_thyao_dortsaat\u001b[49m\u001b[38;5;241m.\u001b[39mdescribe()\n",
      "\u001b[0;31mNameError\u001b[0m: name 'data_thyao_dortsaat' is not defined"
     ]
    }
   ],
   "source": [
    "data_thyao_dortsaat.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'data_thyao_dortsaat' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[6], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mdata_thyao_dortsaat\u001b[49m\u001b[38;5;241m.\u001b[39misnull()\u001b[38;5;241m.\u001b[39msum()\u001b[38;5;241m.\u001b[39msort_values(ascending\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mFalse\u001b[39;00m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'data_thyao_dortsaat' is not defined"
     ]
    }
   ],
   "source": [
    "data_thyao_dortsaat.isnull().sum().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'numpy'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[7], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;66;03m#model deneyelim \u001b[39;00m\n\u001b[0;32m----> 2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mnumpy\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mnp\u001b[39;00m\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m\n\u001b[1;32m      4\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mmatplotlib\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpyplot\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mplt\u001b[39;00m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'numpy'"
     ]
    }
   ],
   "source": [
    "#model deneyelim \n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import plotly.graph_objects as go\n",
    "import os\n",
    "\n",
    "from sklearn.preprocessing import MinMaxScaler\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'data_thyao_dortsaat' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[8], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m df \u001b[38;5;241m=\u001b[39m \u001b[43mdata_thyao_dortsaat\u001b[49m[[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mDate\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mOpen\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mHigh\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mLow\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mClose\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mMACD (26,12)   \u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mTRIGGER (9)   \u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mBOL U (20,2)   \u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mBOL M (20,2)   \u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mBOL D (20,2)   \u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mRSI (14)   \u001b[39m\u001b[38;5;124m'\u001b[39m]]\n\u001b[1;32m      2\u001b[0m df_timestamp \u001b[38;5;241m=\u001b[39m data_thyao_dortsaat[[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mDate\u001b[39m\u001b[38;5;124m\"\u001b[39m]]\n\u001b[1;32m      3\u001b[0m df_ \u001b[38;5;241m=\u001b[39m df[[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mOpen\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mHigh\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mLow\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mClose\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mMACD (26,12)   \u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mTRIGGER (9)   \u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mBOL U (20,2)   \u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mBOL M (20,2)   \u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mBOL D (20,2)   \u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mRSI (14)   \u001b[39m\u001b[38;5;124m'\u001b[39m]]\n",
      "\u001b[0;31mNameError\u001b[0m: name 'data_thyao_dortsaat' is not defined"
     ]
    }
   ],
   "source": [
    "df = data_thyao_dortsaat[['Date', 'Open', 'High', 'Low', 'Close', 'MACD (26,12)   ', 'TRIGGER (9)   ', 'BOL U (20,2)   ', 'BOL M (20,2)   ', 'BOL D (20,2)   ', 'RSI (14)   ']]\n",
    "df_timestamp = data_thyao_dortsaat[[\"Date\"]]\n",
    "df_ = df[['Open', 'High', 'Low', 'Close', 'MACD (26,12)   ', 'TRIGGER (9)   ', 'BOL U (20,2)   ', 'BOL M (20,2)   ', 'BOL D (20,2)   ', 'RSI (14)   ']]\n",
    "#df_ = df[['Close', 'MACD (26,12)   ', 'TRIGGER (9)   ', 'BOL U (20,2)   ', 'BOL M (20,2)   ', 'BOL D (20,2)   ', 'RSI (14)   ']]\n",
    "\n",
    "df_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df_' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[9], line 3\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;66;03m#cols_corr = ['Open', 'High', 'Low', 'Close', 'MACD (26,12)   ', 'TRIGGER (9)   ', 'BOL U (20,2)   ', 'BOL M (20,2)   ', 'BOL D (20,2)   ', 'RSI (14)   ' ,'HOURS', 'MINUTES', 'MINUTES_PASS']\u001b[39;00m\n\u001b[1;32m      2\u001b[0m cols_corr \u001b[38;5;241m=\u001b[39m [\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mClose\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mMACD (26,12)   \u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mTRIGGER (9)   \u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mBOL U (20,2)   \u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mBOL M (20,2)   \u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mBOL D (20,2)   \u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mRSI (14)   \u001b[39m\u001b[38;5;124m'\u001b[39m]\n\u001b[0;32m----> 3\u001b[0m corrMatrix \u001b[38;5;241m=\u001b[39m \u001b[43mdf_\u001b[49m[cols_corr]\u001b[38;5;241m.\u001b[39mcorr()\n\u001b[1;32m      4\u001b[0m plt\u001b[38;5;241m.\u001b[39mfigure(figsize\u001b[38;5;241m=\u001b[39m(\u001b[38;5;241m15\u001b[39m,\u001b[38;5;241m5\u001b[39m))\n\u001b[1;32m      5\u001b[0m fig_corr \u001b[38;5;241m=\u001b[39m sns\u001b[38;5;241m.\u001b[39mheatmap(corrMatrix, annot\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'df_' is not defined"
     ]
    }
   ],
   "source": [
    "#cols_corr = ['Open', 'High', 'Low', 'Close', 'MACD (26,12)   ', 'TRIGGER (9)   ', 'BOL U (20,2)   ', 'BOL M (20,2)   ', 'BOL D (20,2)   ', 'RSI (14)   ' ,'HOURS', 'MINUTES', 'MINUTES_PASS']\n",
    "cols_corr = ['Close', 'MACD (26,12)   ', 'TRIGGER (9)   ', 'BOL U (20,2)   ', 'BOL M (20,2)   ', 'BOL D (20,2)   ', 'RSI (14)   ']\n",
    "corrMatrix = df_[cols_corr].corr()\n",
    "plt.figure(figsize=(15,5))\n",
    "fig_corr = sns.heatmap(corrMatrix, annot=True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df_' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[10], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mdf_\u001b[49m[[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mMACD (26,12)   \u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mTRIGGER (9)   \u001b[39m\u001b[38;5;124m'\u001b[39m]]\n",
      "\u001b[0;31mNameError\u001b[0m: name 'df_' is not defined"
     ]
    }
   ],
   "source": [
    "df_[['MACD (26,12)   ', 'TRIGGER (9)   ']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df_' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[11], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mdf_\u001b[49m[[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mTRIGGER (9)   \u001b[39m\u001b[38;5;124m'\u001b[39m]]\n",
      "\u001b[0;31mNameError\u001b[0m: name 'df_' is not defined"
     ]
    }
   ],
   "source": [
    "df_[['TRIGGER (9)   ']]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "MACD ile Trigger arasındaki bağlantı\n",
    "MACD ile Trigger arasındaki bağlantıyı koda yansıtılması lazım\n",
    "\n",
    "Sonuçları is_bigger sütununa eklenecek\n",
    "İki değerde 0 ın altında iken MACD'nin Triggerı geçtiği kesinti anındaki ilk an 1 döndürülmeli\n",
    "İki değerin herhangi kesme durumu olmadığı durumlarda 0 döndürmeli\n",
    "İki değerde 1 in üstündeyken MACD'nin Trigger'dan az olduğu kesinti anındaki ilk an -1 döndürülmeli\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df_' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[12], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;66;03m#İstenilen algoritma \u001b[39;00m\n\u001b[0;32m----> 2\u001b[0m \u001b[43mdf_\u001b[49m[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mis_bigger\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m0\u001b[39m\n\u001b[1;32m      4\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m(\u001b[38;5;241m1\u001b[39m, \u001b[38;5;28mlen\u001b[39m(df_)):\n\u001b[1;32m      5\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m (df_[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mMACD (26,12)   \u001b[39m\u001b[38;5;124m'\u001b[39m][i] \u001b[38;5;241m>\u001b[39m \u001b[38;5;241m0\u001b[39m \u001b[38;5;129;01mand\u001b[39;00m df_[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mTRIGGER (9)   \u001b[39m\u001b[38;5;124m'\u001b[39m][i] \u001b[38;5;241m>\u001b[39m \u001b[38;5;241m0\u001b[39m):\n",
      "\u001b[0;31mNameError\u001b[0m: name 'df_' is not defined"
     ]
    }
   ],
   "source": [
    "#İstenilen algoritma \n",
    "df_['is_bigger'] = 0\n",
    "\n",
    "for i in range(1, len(df_)):\n",
    "    if (df_['MACD (26,12)   '][i] > 0 and df_['TRIGGER (9)   '][i] > 0):\n",
    "        if (df_['MACD (26,12)   '][i] < df_['TRIGGER (9)   '][i] and df_['MACD (26,12)   '][i-1] >= df_['TRIGGER (9)   '][i-1]):\n",
    "            df_['is_bigger'][i] = -1\n",
    "    elif (df_['MACD (26,12)   '][i] < 0 and df_['TRIGGER (9)   '][i] < 0):\n",
    "        if (df_['MACD (26,12)   '][i] > df_['TRIGGER (9)   '][i] and df_['MACD (26,12)   '][i-1] <= df_['TRIGGER (9)   '][i-1]):\n",
    "            df_['is_bigger'][i] = 1\n",
    "\n",
    "df_['is_bigger']\n",
    "\n",
    "        \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df_' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[13], line 48\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;124;03m\"\"\"Stokastik RSI (Stochastic Relative Strength Index), geleneksel RSI göstergesinin stokastik osilatör ile birleştirilmiş halidir. Bu gösterge, fiyatların belirli bir zaman dilimindeki göreceli gücünü ölçmek için kullanılır ve daha hassas alım satım sinyalleri üretebilir. Stokastik RSI, RSI değerlerini stokastik osilatör formülüyle hesaplayarak, RSI'nın aşırı alım ve aşırı satım seviyelerini daha hızlı ve daha duyarlı bir şekilde tespit etmeyi sağlar.\u001b[39;00m\n\u001b[1;32m      2\u001b[0m \n\u001b[1;32m      3\u001b[0m \u001b[38;5;124;03mStokastik RSI Nedir?\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m     45\u001b[0m \u001b[38;5;124;03msatış sinyalinde -1\u001b[39;00m\n\u001b[1;32m     46\u001b[0m \u001b[38;5;124;03maşırı satış sinyalinde -2  \"\"\"\u001b[39;00m\n\u001b[0;32m---> 48\u001b[0m \u001b[43mdf_\u001b[49m[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mstoch_rsi\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m0\u001b[39m\n\u001b[1;32m     50\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m(\u001b[38;5;241m1\u001b[39m, \u001b[38;5;28mlen\u001b[39m(df_)):\n\u001b[1;32m     51\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m (df_[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mRSI (14)   \u001b[39m\u001b[38;5;124m'\u001b[39m][i] \u001b[38;5;241m>\u001b[39m \u001b[38;5;241m80\u001b[39m):\n",
      "\u001b[0;31mNameError\u001b[0m: name 'df_' is not defined"
     ]
    }
   ],
   "source": [
    "\"\"\"Stokastik RSI (Stochastic Relative Strength Index), geleneksel RSI göstergesinin stokastik osilatör ile birleştirilmiş halidir. Bu gösterge, fiyatların belirli bir zaman dilimindeki göreceli gücünü ölçmek için kullanılır ve daha hassas alım satım sinyalleri üretebilir. Stokastik RSI, RSI değerlerini stokastik osilatör formülüyle hesaplayarak, RSI'nın aşırı alım ve aşırı satım seviyelerini daha hızlı ve daha duyarlı bir şekilde tespit etmeyi sağlar.\n",
    "\n",
    "Stokastik RSI Nedir?\n",
    "\n",
    "Stokastik RSI, RSI değerlerinin stokastik osilatör formülü kullanılarak hesaplanmasıyla elde edilir. Bu, yatırımcılara geleneksel RSI'ya göre daha hassas sinyaller sağlar ve kısa vadeli fiyat hareketlerini daha iyi analiz etmelerine yardımcı olur.\n",
    "\n",
    "Stokastik RSI Nasıl Hesaplanır?\n",
    "\n",
    "Stokastik RSI hesaplaması şu adımlarla yapılır:\n",
    "\n",
    "1. RSI Hesaplanması: İlk olarak, belirlenen zaman dilimi için RSI değerleri hesaplanır.\n",
    "\n",
    "2. Stokastik RSI Hesaplanması: Daha sonra, bu RSI değerleri stokastik osilatör formülü ile işlenir:\n",
    "\n",
    "Stokastik RSI=RSI−Minimum RSIMaksimum RSI−Minimum RSI\\text{Stokastik RSI} = \\frac{\\text{RSI} - \\text{Minimum RSI}}{\\text{Maksimum RSI} - \\text{Minimum RSI}}Stokastik RSI=Maksimum RSI−Minimum RSIRSI−Minimum RSI\n",
    "\n",
    "Bu formül, RSI değerlerinin belirli bir dönem içindeki en düşük ve en yüksek değerleri arasındaki konumunu belirler.\n",
    "\n",
    "Stokastik RSI Nasıl Kullanılır?\n",
    "\n",
    "Stokastik RSI, genellikle aşırı alım ve aşırı satım seviyelerini belirlemek için kullanılır. Kullanım şekli geleneksel RSI ve stokastik osilatöre benzerdir:\n",
    "\n",
    "1. Aşırı Alım ve Aşırı Satım Seviyeleri:\n",
    "\n",
    "o Aşırı Alım: Stokastik RSI değeri 80'in üzerinde ise, varlık aşırı alım bölgesinde kabul edilir ve fiyatların düşme olasılığı artar.\n",
    "\n",
    "o Aşırı Satım: Stokastik RSI değeri 20'nin altında ise, varlık aşırı satım bölgesinde kabul edilir ve fiyatların yükselme olasılığı artar.\n",
    "\n",
    "2. Uyumsuzluklar (Diverjans):\n",
    "\n",
    "o Boğa Uyumsuzluğu (Bullish Divergence): Fiyatlar düşerken stokastik RSI yükseliyorsa, bu fiyatların toparlanabileceğine işaret eder.\n",
    "\n",
    "o Ayı Uyumsuzluğu (Bearish Divergence): Fiyatlar yükselirken stokastik RSI düşüyorsa, bu fiyatların düşebileceğine işaret eder.\n",
    "\n",
    "3. Kesişimler (Crossovers):\n",
    "\n",
    "o Alış Sinyali: Stokastik RSI değeri 20'nin altına düştüğünde ve sonra tekrar yukarıya doğru geçtiğinde alış sinyali oluşur.\n",
    "\n",
    "o Satış Sinyali: Stokastik RSI değeri 80'in üzerine çıktığında ve sonra tekrar aşağıya doğru geçtiğinde satış sinyali oluşur.\n",
    "\n",
    "\n",
    "aşırı alım sinyalinde +2 \n",
    "alım sinyalinde +1\n",
    "normal seyirde 0 ü\n",
    "satış sinyalinde -1\n",
    "aşırı satış sinyalinde -2 \n",
    "\n",
    "\n",
    "#İstenilen algoritma \n",
    "df_['is_bigger'] = 0\n",
    "\n",
    "for i in range(1, len(df_)):\n",
    "    if (df_['MACD (26,12)   '][i] > 0 and df_['TRIGGER (9)   '][i] > 0):\n",
    "        if (df_['MACD (26,12)   '][i] < df_['TRIGGER (9)   '][i] and df_['MACD (26,12)   '][i-1] >= df_['TRIGGER (9)   '][i-1]):\n",
    "            df_['is_bigger'][i] = -1\n",
    "    elif (df_['MACD (26,12)   '][i] < 0 and df_['TRIGGER (9)   '][i] < 0):\n",
    "        if (df_['MACD (26,12)   '][i] > df_['TRIGGER (9)   '][i] and df_['MACD (26,12)   '][i-1] <= df_['TRIGGER (9)   '][i-1]):\n",
    "            df_['is_bigger'][i] = 1\n",
    "\n",
    "df_['is_bigger'] benzer algoritma ile stokastik rsi için de yapılabilir.\"\"\"\n",
    "\n",
    "#stokastik rsi\n",
    "df_['stoch_rsi'] = 0\n",
    "\n",
    "for i in range(1, len(df_)):\n",
    "    if (df_['RSI (14)   '][i] > 80):\n",
    "        df_['stoch_rsi'][i] = -2\n",
    "    elif (df_['RSI (14)   '][i] > 70):\n",
    "        df_['stoch_rsi'][i] = -1\n",
    "    elif (df_['RSI (14)   '][i] < 20):\n",
    "        df_['stoch_rsi'][i] = 2\n",
    "    elif (df_['RSI (14)   '][i] < 30):\n",
    "        df_['stoch_rsi'][i] = 1\n",
    "    \n",
    "df_['stoch_rsi']\n",
    "\n",
    "# 0 ile 30. satırları  df_['stoch_rsi'] yazdırma \n",
    "df_['stoch_rsi'][0:30]\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2612106681.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[3], line 1\u001b[0;36m\u001b[0m\n\u001b[0;31m    ADX (Average Directional Index) ve DMI (Directional Movement Index), J. Welles Wilder tarafından geliştirilmiş teknik analiz göstergeleridir. Bu göstergeler, bir varlığın fiyat hareketlerinin gücünü ve yönünü belirlemeye yardımcı olur. ADX, bir trendin gücünü ölçerken, DMI, trendin yönünü belirlemeye çalışır.\u001b[0m\n\u001b[0m                 ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "\"\"\"ADX (Average Directional Index) ve DMI (Directional Movement Index), J. Welles Wilder tarafından geliştirilmiş teknik analiz göstergeleridir. Bu göstergeler, bir varlığın fiyat hareketlerinin gücünü ve yönünü belirlemeye yardımcı olur. ADX, bir trendin gücünü ölçerken, DMI, trendin yönünü belirlemeye çalışır.\n",
    "\n",
    "ADX (Average Directional Index) Nedir ve Nasıl Çalışır?\n",
    "\n",
    "ADX, bir trendin gücünü belirlemek için kullanılan bir göstergedir. ADX'in değerleri 0 ile 100 arasında değişir ve genellikle 20'nin üzerindeki değerler güçlü bir trendi, 20'nin altındaki değerler ise zayıf bir trendi gösterir.\n",
    "\n",
    "ADX Nasıl Hesaplanır?\n",
    "\n",
    "1. True Range (TR) Hesaplama:\n",
    "\n",
    "o TR, mevcut yüksek ile mevcut düşük arasındaki fark, mevcut yüksek ile önceki kapanış arasındaki fark ve mevcut düşük ile önceki kapanış arasındaki farkın en büyüğüdür.\n",
    "\n",
    "2. Directional Movement (DM) Hesaplama:\n",
    "\n",
    "o Positive Directional Movement (+DM): Mevcut yüksek, önceki yüksekten büyükse ve mevcut düşük, önceki düşükten küçükse hesaplanır.\n",
    "\n",
    "o Negative Directional Movement (-DM): Mevcut düşük, önceki düşükten küçükse ve mevcut yüksek, önceki yüksekten küçükse hesaplanır.\n",
    "\n",
    "3. Directional Movement Index (DMI) Hesaplama:\n",
    "\n",
    "o +DI ve -DI değerleri, +DM ve -DM'nin belirli bir süre (genellikle 14 gün) boyunca ortalamasının ATR'ye (Average True Range) bölünmesiyle hesaplanır.\n",
    "\n",
    "o +DI ve -DI, belirli bir süre boyunca (genellikle 14 gün) ortalaması alınarak normalize edilir.\n",
    "\n",
    "4. ADX Hesaplama:\n",
    "\n",
    "o ADX, +DI ve -DI arasındaki farkın toplamının ortalamasının hesaplanmasıyla elde edilir.\n",
    "\n",
    "ADX=Hareketli Ortalama(∣+DI−-DI∣+DI+-DI×100)\\text{ADX} = \\text{Hareketli Ortalama}\\left(\\frac{|\\text{+DI} - \\text{-DI}|}{\\text{+DI} + \\text{-DI}} \\times 100 \\right)ADX=Hareketli Ortalama(+DI+-DI∣+DI−-DI∣×100)\n",
    "\n",
    "DMI (Directional Movement Index) Nedir ve Nasıl Çalışır?\n",
    "\n",
    "DMI, ADX ile birlikte kullanılarak bir trendin yönünü ve gücünü belirlemek için kullanılır. DMI, iki ana bileşenden oluşur: +DI ve -DI.\n",
    "\n",
    "· +DI (Positive Directional Indicator): Belirli bir dönemdeki pozitif yönlü hareketleri gösterir.\n",
    "\n",
    "· -DI (Negative Directional Indicator): Belirli bir dönemdeki negatif yönlü hareketleri gösterir.\n",
    "\n",
    "ADX ve DMI Nasıl Kullanılır?\n",
    "\n",
    "1. Trendin Gücünü Belirleme:\n",
    "\n",
    "o ADX, 20'nin üzerinde ise güçlü bir trend olduğunu gösterir. ADX, 40'ın üzerinde ise çok güçlü bir trend olduğunu gösterebilir.\n",
    "\n",
    "o ADX, 20'nin altında ise trendin zayıf olduğunu gösterir.\n",
    "\n",
    "2. Trendin Yönünü Belirleme:\n",
    "\n",
    "o +DI, -DI'nin üzerindeyse yükseliş trendi olduğunu gösterir.\n",
    "\n",
    "o -DI, +DI'nin üzerindeyse düşüş trendi olduğunu gösterir.\n",
    "\n",
    "3. Kesişim Sinyalleri:\n",
    "\n",
    "o +DI, -DI'yi yukarı keserse, bu bir alış sinyali olabilir.\n",
    "\n",
    "o -DI, +DI'yi yukarı keserse, bu bir satış sinyali olabilir.\n",
    "\n",
    "Örnek Kullanım\n",
    "\n",
    "Örneğin, 14 günlük bir ADX ve DMI hesaplamak için şu adımları izleyebilirsiniz:\n",
    "\n",
    "1. True Range (TR) Hesaplama:\n",
    "\n",
    "o Son 14 günün TR değerlerini hesaplayın.\n",
    "\n",
    "2. Directional Movement (DM) Hesaplama:\n",
    "\n",
    "o Son 14 günün +DM ve -DM değerlerini hesaplayın.\n",
    "\n",
    "3. +DI ve -DI Hesaplama:\n",
    "\n",
    "o +DI ve -DI değerlerini hesaplayın ve normalize edin.\n",
    "\n",
    "4. ADX Hesaplama:\n",
    "\n",
    "o ADX değerini hesaplayın ve grafikte gösterin.\n",
    "\n",
    "ADX ve DMI ile İlgili Notlar\n",
    "\n",
    "· Sinyallerin Güvenilirliği: ADX ve DMI, piyasa koşullarına bağlı olarak yanlış sinyaller verebilir. Bu nedenle diğer teknik göstergeler ve analiz yöntemleri ile birlikte kullanılması önerilir.\n",
    "\n",
    "· Farklı Zaman Dilimleri: ADX ve DMI, farklı zaman dilimlerinde kullanılabilir. Ancak, daha uzun zaman dilimleri daha güvenilir sinyaller verebilir.\n",
    "\n",
    "· Volatilite: Yüksek volatilite dönemlerinde ADX ve DMI daha fazla sinyal üretebilir, bu nedenle dikkatli kullanılmalıdır.\n",
    "\n",
    "ADX ve DMI, yatırımcıların trendleri daha iyi anlamalarına ve doğru alım-satım kararları vermelerine yardımcı olabilir. Ancak, her teknik analiz aracında olduğu gibi, tek başına kullanılmamalı ve diğer analiz araçları ile birlikte değerlendirilmelidir.\n",
    "\n",
    "ÖZETLE Adx ve dmı indikatörü iç içedir ve birlikte kullanılır.\n",
    "\n",
    "Adx çizgi hareketleri grafiğin yönünü göstermez. Trend olduğunu ve trendin gücünü belirtir.Genel olarak 25in üzerinde ise trend güçlenmeye başlar demek. Grafik 15in altına inerse yeni trend olabilir anlamına geliyor diye yorumlayabilirz.\n",
    "\n",
    "DMI indikatöründe adx çizgi değerleri de vardır. +dı ve -dı olmak üzere 3 çizgi vardır.\n",
    "\n",
    "+DI -DI çizgisinin üztüne çıkarsa grafik hareketleri yukarı çıkacağını gösterir. +DI ve -DI birbirinden ayrıldıkça grafikte hareketlenme fazla olur.\n",
    "\n",
    "ADX, +DI ve -DI arasındaki farkın toplamının ortalamasının hesaplanmasıyla elde edili\n",
    "(KODU YAPILACAK)\n",
    "\n",
    "yükseliş trendinde 1 \n",
    "normal zamanda 0 \n",
    "düşüş trendinde -1 \n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df[['Date', 'High', 'Low', 'Close', 'ADX (14)   ', 'adx_dmi']]  nasıl 70 ile 100 arasındaki sütunları yazdırma\n",
    "\n",
    "df[['Date', 'High', 'Low', 'Close', 'ADX (14)   ', 'adx_dmi']][70:100]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "KDJ (Stochastic Oscillator with a twist of RSI) indikatörü, teknik analizde kullanılan bir göstergedir ve özellikle Asya piyasalarında popülerdir. KDJ, stokastik osilatör ve RSI göstergelerinin birleşimidir ve fiyatların aşırı alım ve aşırı satım seviyelerini belirlemek için kullanılır. KDJ, üç ana bileşenden oluşur: %K, %D ve %J.\n",
    "\n",
    "KDJ İndikatörü Nedir?\n",
    "\n",
    "KDJ, temel olarak stokastik osilatörün bir varyasyonudur ve aşağıdaki bileşenlerden oluşur:\n",
    "\n",
    "· %K: Stokastik osilatörün ana hattıdır ve kapanış fiyatlarının belirli bir süre içindeki en yüksek ve en düşük fiyatlarla nasıl karşılaştırıldığını gösterir.\n",
    "\n",
    "· %D: %K'nın hareketli ortalamasıdır ve daha yumuşak bir çizgi sağlar.\n",
    "\n",
    "· %J: %K ve %D değerlerinin birleşiminden elde edilen bir bileşendir ve genellikle daha volatil bir hattır.\n",
    "\n",
    "KDJ İndikatörü Nasıl Hesaplanır?\n",
    "\n",
    "KDJ indikatörünün hesaplanması şu adımları içerir:\n",
    "\n",
    "1. %K Hesaplama:\n",
    "\n",
    "%K=(C−Ln)(Hn−Ln)×100\\%K = \\frac{(C - L_{n})}{(H_{n} - L_{n})} \\times 100%K=(Hn−Ln)(C−Ln)×100\n",
    "\n",
    "Burada:\n",
    "\n",
    "o CCC: Mevcut kapanış fiyatı\n",
    "\n",
    "o LnL_{n}Ln: Belirli bir dönem içindeki en düşük fiyat\n",
    "\n",
    "o HnH_{n}Hn: Belirli bir dönem içindeki en yüksek fiyat\n",
    "\n",
    "o nnn: Hesaplama için kullanılan dönem sayısı (genellikle 14 gün)\n",
    "\n",
    "2. %D Hesaplama:\n",
    "\n",
    "%D=SMA(%K,3)\\%D = \\text{SMA}(\\%K, 3)%D=SMA(%K,3)\n",
    "\n",
    "Burada SMA, %K'nın 3 dönemlik basit hareketli ortalamasıdır.\n",
    "\n",
    "3. %J Hesaplama:\n",
    "\n",
    "%J=3×%K−2×%D\\%J = 3 \\times \\%K - 2 \\times \\%D%J=3×%K−2×%D\n",
    "\n",
    "KDJ İndikatörü Nasıl Kullanılır?\n",
    "\n",
    "KDJ indikatörü, aşağıdaki yollarla kullanılabilir:\n",
    "\n",
    "1. Aşırı Alım ve Aşırı Satım Seviyeleri:\n",
    "\n",
    "o Aşırı Alım: %K veya %J değeri 80'in üzerindeyse, varlık aşırı alım bölgesinde kabul edilir ve fiyatların düşme olasılığı artar.\n",
    "\n",
    "o Aşırı Satım: %K veya %J değeri 20'nin altındaysa, varlık aşırı satım bölgesinde kabul edilir ve fiyatların yükselme olasılığı artar.\n",
    "\n",
    "2. Kesişimler (Crossovers):\n",
    "\n",
    "o Alış Sinyali: %K hattı %D hattını alttan yukarı keserse, bu bir alış sinyali olarak yorumlanabilir.\n",
    "\n",
    "o Satış Sinyali: %K hattı %D hattını üstten aşağı keserse, bu bir satış sinyali olarak yorumlanabilir.\n",
    "\n",
    "3. %J Değeri:\n",
    "\n",
    "o %J değeri, aşırı alım ve aşırı satım seviyelerini daha aşırı noktalara taşır ve genellikle daha volatil bir göstergedir. %J değeri 100'ün üzerinde veya 0'ın altında olabilir, bu da aşırı alım ve aşırı satım sinyallerini daha belirgin hale getirir.\n",
    "\n",
    "Örnek Kullanım\n",
    "\n",
    "Örneğin, bir hisse senedinin kapanış fiyatları kullanılarak 14 günlük bir KDJ indikatörü hesaplamak için şu adımları izleyebilirsiniz:\n",
    "\n",
    "1. %K Hesaplama:\n",
    "\n",
    "o Son 14 günün en yüksek ve en düşük fiyatlarını belirleyin.\n",
    "\n",
    "o %K değerini hesaplayın.\n",
    "\n",
    "2. %D Hesaplama:\n",
    "\n",
    "o %K değerinin 3 günlük basit hareketli ortalamasını hesaplayın.\n",
    "\n",
    "3. %J Hesaplama:\n",
    "\n",
    "o %J değerini hesaplamak için %K ve %D değerlerini kullanın.\n",
    "\n",
    "KDJ İndikatörü ile İlgili Notlar\n",
    "\n",
    "· Volatilite: %J bileşeni, diğer bileşenlere göre daha volatil olabilir ve bu nedenle daha sık alım-satım sinyalleri üretebilir.\n",
    "\n",
    "· Diğer Göstergelerle Kombinasyon: KDJ, diğer teknik analiz araçları ve göstergelerle birlikte kullanıldığında daha güvenilir sonuçlar verebilir.\n",
    "\n",
    "· Zaman Çerçevesi: Farklı zaman dilimlerinde KDJ göstergesinin performansı farklı olabilir, bu nedenle kullanılan zaman dilimi dikkatle seçilmelidir.\n",
    "\n",
    "KDJ indikatörü, yatırımcılara piyasa hareketlerini daha iyi anlamaları ve doğru alım-satım kararları vermeleri konusunda yardımcı olabilir. Ancak, her teknik gösterge gibi, tek başına kullanıldığında hatalı sinyaller verebileceği için diğer analiz araçları ile birlikte değerlendirilmelidir.\n",
    "\n",
    "Kısaca KDJ kısa vade ve uzun vade de etkili olabilir. MACD ile benzetilebilir ama macdden genel olarak önce sinyal verebilir.\n",
    "\n",
    "Siyah çizgi mavi ve kırmızıyı yukarı yönlü kesiyorsa buna golden cross denir ve al sinyali demektir. Aşağı yonlu keserse death cross denilen sat sinyali demektir.\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "aşırı alım sinyalinde +2 \n",
    "alım sinyalinde +1\n",
    "normal seyirde 0 ü\n",
    "satış sinyalinde -1\n",
    "aşırı satış sinyalinde -2 \n",
    "\n",
    "\n",
    "#İstenilen algoritma  KDJ (Stochastic Oscillator with a twist of RSI)\n",
    "\n",
    "\n",
    "            \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
