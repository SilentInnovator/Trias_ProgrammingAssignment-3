{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8972db13-0d9b-4bc3-a5dd-b186cf1bbb88",
   "metadata": {},
   "source": [
    "# Trias_Pandas-P2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d36330e4-0732-4ae9-a83b-63e72ab25c8e",
   "metadata": {},
   "source": [
    "#### Using the dataframe cars in problem 1, extract the following information using subsetting, \n",
    "#### slicing and indexing operations.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d7620acf-27d8-4b47-af3d-61e8b45a95bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b5019117-0a2c-414f-86ee-8b7638b2d5e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.90</td>\n",
       "      <td>2.620</td>\n",
       "      <td>16.46</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.90</td>\n",
       "      <td>2.875</td>\n",
       "      <td>17.02</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Datsun 710</td>\n",
       "      <td>22.8</td>\n",
       "      <td>4</td>\n",
       "      <td>108.0</td>\n",
       "      <td>93</td>\n",
       "      <td>3.85</td>\n",
       "      <td>2.320</td>\n",
       "      <td>18.61</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hornet 4 Drive</td>\n",
       "      <td>21.4</td>\n",
       "      <td>6</td>\n",
       "      <td>258.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.08</td>\n",
       "      <td>3.215</td>\n",
       "      <td>19.44</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Hornet Sportabout</td>\n",
       "      <td>18.7</td>\n",
       "      <td>8</td>\n",
       "      <td>360.0</td>\n",
       "      <td>175</td>\n",
       "      <td>3.15</td>\n",
       "      <td>3.440</td>\n",
       "      <td>17.02</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Valiant</td>\n",
       "      <td>18.1</td>\n",
       "      <td>6</td>\n",
       "      <td>225.0</td>\n",
       "      <td>105</td>\n",
       "      <td>2.76</td>\n",
       "      <td>3.460</td>\n",
       "      <td>20.22</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Duster 360</td>\n",
       "      <td>14.3</td>\n",
       "      <td>8</td>\n",
       "      <td>360.0</td>\n",
       "      <td>245</td>\n",
       "      <td>3.21</td>\n",
       "      <td>3.570</td>\n",
       "      <td>15.84</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Merc 240D</td>\n",
       "      <td>24.4</td>\n",
       "      <td>4</td>\n",
       "      <td>146.7</td>\n",
       "      <td>62</td>\n",
       "      <td>3.69</td>\n",
       "      <td>3.190</td>\n",
       "      <td>20.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Merc 230</td>\n",
       "      <td>22.8</td>\n",
       "      <td>4</td>\n",
       "      <td>140.8</td>\n",
       "      <td>95</td>\n",
       "      <td>3.92</td>\n",
       "      <td>3.150</td>\n",
       "      <td>22.90</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Merc 280</td>\n",
       "      <td>19.2</td>\n",
       "      <td>6</td>\n",
       "      <td>167.6</td>\n",
       "      <td>123</td>\n",
       "      <td>3.92</td>\n",
       "      <td>3.440</td>\n",
       "      <td>18.30</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Merc 280C</td>\n",
       "      <td>17.8</td>\n",
       "      <td>6</td>\n",
       "      <td>167.6</td>\n",
       "      <td>123</td>\n",
       "      <td>3.92</td>\n",
       "      <td>3.440</td>\n",
       "      <td>18.90</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Merc 450SE</td>\n",
       "      <td>16.4</td>\n",
       "      <td>8</td>\n",
       "      <td>275.8</td>\n",
       "      <td>180</td>\n",
       "      <td>3.07</td>\n",
       "      <td>4.070</td>\n",
       "      <td>17.40</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Merc 450SL</td>\n",
       "      <td>17.3</td>\n",
       "      <td>8</td>\n",
       "      <td>275.8</td>\n",
       "      <td>180</td>\n",
       "      <td>3.07</td>\n",
       "      <td>3.730</td>\n",
       "      <td>17.60</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Merc 450SLC</td>\n",
       "      <td>15.2</td>\n",
       "      <td>8</td>\n",
       "      <td>275.8</td>\n",
       "      <td>180</td>\n",
       "      <td>3.07</td>\n",
       "      <td>3.780</td>\n",
       "      <td>18.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Cadillac Fleetwood</td>\n",
       "      <td>10.4</td>\n",
       "      <td>8</td>\n",
       "      <td>472.0</td>\n",
       "      <td>205</td>\n",
       "      <td>2.93</td>\n",
       "      <td>5.250</td>\n",
       "      <td>17.98</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>Lincoln Continental</td>\n",
       "      <td>10.4</td>\n",
       "      <td>8</td>\n",
       "      <td>460.0</td>\n",
       "      <td>215</td>\n",
       "      <td>3.00</td>\n",
       "      <td>5.424</td>\n",
       "      <td>17.82</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Chrysler Imperial</td>\n",
       "      <td>14.7</td>\n",
       "      <td>8</td>\n",
       "      <td>440.0</td>\n",
       "      <td>230</td>\n",
       "      <td>3.23</td>\n",
       "      <td>5.345</td>\n",
       "      <td>17.42</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Fiat 128</td>\n",
       "      <td>32.4</td>\n",
       "      <td>4</td>\n",
       "      <td>78.7</td>\n",
       "      <td>66</td>\n",
       "      <td>4.08</td>\n",
       "      <td>2.200</td>\n",
       "      <td>19.47</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Honda Civic</td>\n",
       "      <td>30.4</td>\n",
       "      <td>4</td>\n",
       "      <td>75.7</td>\n",
       "      <td>52</td>\n",
       "      <td>4.93</td>\n",
       "      <td>1.615</td>\n",
       "      <td>18.52</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>Toyota Corolla</td>\n",
       "      <td>33.9</td>\n",
       "      <td>4</td>\n",
       "      <td>71.1</td>\n",
       "      <td>65</td>\n",
       "      <td>4.22</td>\n",
       "      <td>1.835</td>\n",
       "      <td>19.90</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Toyota Corona</td>\n",
       "      <td>21.5</td>\n",
       "      <td>4</td>\n",
       "      <td>120.1</td>\n",
       "      <td>97</td>\n",
       "      <td>3.70</td>\n",
       "      <td>2.465</td>\n",
       "      <td>20.01</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Dodge Challenger</td>\n",
       "      <td>15.5</td>\n",
       "      <td>8</td>\n",
       "      <td>318.0</td>\n",
       "      <td>150</td>\n",
       "      <td>2.76</td>\n",
       "      <td>3.520</td>\n",
       "      <td>16.87</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>AMC Javelin</td>\n",
       "      <td>15.2</td>\n",
       "      <td>8</td>\n",
       "      <td>304.0</td>\n",
       "      <td>150</td>\n",
       "      <td>3.15</td>\n",
       "      <td>3.435</td>\n",
       "      <td>17.30</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>Camaro Z28</td>\n",
       "      <td>13.3</td>\n",
       "      <td>8</td>\n",
       "      <td>350.0</td>\n",
       "      <td>245</td>\n",
       "      <td>3.73</td>\n",
       "      <td>3.840</td>\n",
       "      <td>15.41</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>Pontiac Firebird</td>\n",
       "      <td>19.2</td>\n",
       "      <td>8</td>\n",
       "      <td>400.0</td>\n",
       "      <td>175</td>\n",
       "      <td>3.08</td>\n",
       "      <td>3.845</td>\n",
       "      <td>17.05</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>Fiat X1-9</td>\n",
       "      <td>27.3</td>\n",
       "      <td>4</td>\n",
       "      <td>79.0</td>\n",
       "      <td>66</td>\n",
       "      <td>4.08</td>\n",
       "      <td>1.935</td>\n",
       "      <td>18.90</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>Porsche 914-2</td>\n",
       "      <td>26.0</td>\n",
       "      <td>4</td>\n",
       "      <td>120.3</td>\n",
       "      <td>91</td>\n",
       "      <td>4.43</td>\n",
       "      <td>2.140</td>\n",
       "      <td>16.70</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>Lotus Europa</td>\n",
       "      <td>30.4</td>\n",
       "      <td>4</td>\n",
       "      <td>95.1</td>\n",
       "      <td>113</td>\n",
       "      <td>3.77</td>\n",
       "      <td>1.513</td>\n",
       "      <td>16.90</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Ford Pantera L</td>\n",
       "      <td>15.8</td>\n",
       "      <td>8</td>\n",
       "      <td>351.0</td>\n",
       "      <td>264</td>\n",
       "      <td>4.22</td>\n",
       "      <td>3.170</td>\n",
       "      <td>14.50</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>Ferrari Dino</td>\n",
       "      <td>19.7</td>\n",
       "      <td>6</td>\n",
       "      <td>145.0</td>\n",
       "      <td>175</td>\n",
       "      <td>3.62</td>\n",
       "      <td>2.770</td>\n",
       "      <td>15.50</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>Maserati Bora</td>\n",
       "      <td>15.0</td>\n",
       "      <td>8</td>\n",
       "      <td>301.0</td>\n",
       "      <td>335</td>\n",
       "      <td>3.54</td>\n",
       "      <td>3.570</td>\n",
       "      <td>14.60</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>Volvo 142E</td>\n",
       "      <td>21.4</td>\n",
       "      <td>4</td>\n",
       "      <td>121.0</td>\n",
       "      <td>109</td>\n",
       "      <td>4.11</td>\n",
       "      <td>2.780</td>\n",
       "      <td>18.60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  \\\n",
       "0             Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1   \n",
       "1         Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1   \n",
       "2            Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1   \n",
       "3        Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0   \n",
       "4     Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0   \n",
       "5               Valiant  18.1    6  225.0  105  2.76  3.460  20.22   1   0   \n",
       "6            Duster 360  14.3    8  360.0  245  3.21  3.570  15.84   0   0   \n",
       "7             Merc 240D  24.4    4  146.7   62  3.69  3.190  20.00   1   0   \n",
       "8              Merc 230  22.8    4  140.8   95  3.92  3.150  22.90   1   0   \n",
       "9              Merc 280  19.2    6  167.6  123  3.92  3.440  18.30   1   0   \n",
       "10            Merc 280C  17.8    6  167.6  123  3.92  3.440  18.90   1   0   \n",
       "11           Merc 450SE  16.4    8  275.8  180  3.07  4.070  17.40   0   0   \n",
       "12           Merc 450SL  17.3    8  275.8  180  3.07  3.730  17.60   0   0   \n",
       "13          Merc 450SLC  15.2    8  275.8  180  3.07  3.780  18.00   0   0   \n",
       "14   Cadillac Fleetwood  10.4    8  472.0  205  2.93  5.250  17.98   0   0   \n",
       "15  Lincoln Continental  10.4    8  460.0  215  3.00  5.424  17.82   0   0   \n",
       "16    Chrysler Imperial  14.7    8  440.0  230  3.23  5.345  17.42   0   0   \n",
       "17             Fiat 128  32.4    4   78.7   66  4.08  2.200  19.47   1   1   \n",
       "18          Honda Civic  30.4    4   75.7   52  4.93  1.615  18.52   1   1   \n",
       "19       Toyota Corolla  33.9    4   71.1   65  4.22  1.835  19.90   1   1   \n",
       "20        Toyota Corona  21.5    4  120.1   97  3.70  2.465  20.01   1   0   \n",
       "21     Dodge Challenger  15.5    8  318.0  150  2.76  3.520  16.87   0   0   \n",
       "22          AMC Javelin  15.2    8  304.0  150  3.15  3.435  17.30   0   0   \n",
       "23           Camaro Z28  13.3    8  350.0  245  3.73  3.840  15.41   0   0   \n",
       "24     Pontiac Firebird  19.2    8  400.0  175  3.08  3.845  17.05   0   0   \n",
       "25            Fiat X1-9  27.3    4   79.0   66  4.08  1.935  18.90   1   1   \n",
       "26        Porsche 914-2  26.0    4  120.3   91  4.43  2.140  16.70   0   1   \n",
       "27         Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.90   1   1   \n",
       "28       Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.50   0   1   \n",
       "29         Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.50   0   1   \n",
       "30        Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.60   0   1   \n",
       "31           Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.60   1   1   \n",
       "\n",
       "    gear  carb  \n",
       "0      4     4  \n",
       "1      4     4  \n",
       "2      4     1  \n",
       "3      3     1  \n",
       "4      3     2  \n",
       "5      3     1  \n",
       "6      3     4  \n",
       "7      4     2  \n",
       "8      4     2  \n",
       "9      4     4  \n",
       "10     4     4  \n",
       "11     3     3  \n",
       "12     3     3  \n",
       "13     3     3  \n",
       "14     3     4  \n",
       "15     3     4  \n",
       "16     3     4  \n",
       "17     4     1  \n",
       "18     4     2  \n",
       "19     4     1  \n",
       "20     3     1  \n",
       "21     3     2  \n",
       "22     3     2  \n",
       "23     3     4  \n",
       "24     3     2  \n",
       "25     4     1  \n",
       "26     5     2  \n",
       "27     5     2  \n",
       "28     5     4  \n",
       "29     5     6  \n",
       "30     5     8  \n",
       "31     4     2  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cars = pd.read_csv('cars.csv')\n",
    "cars"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b3c9a6c-9bd6-4f8b-b9d5-18f3f2721c34",
   "metadata": {},
   "source": [
    "#### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "053b58ab-2f30-408c-914f-1cd12cf8f862",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "      <th>hp</th>\n",
       "      <th>wt</th>\n",
       "      <th>vs</th>\n",
       "      <th>gear</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>6</td>\n",
       "      <td>110</td>\n",
       "      <td>2.620</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>6</td>\n",
       "      <td>110</td>\n",
       "      <td>2.875</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Datsun 710</td>\n",
       "      <td>4</td>\n",
       "      <td>93</td>\n",
       "      <td>2.320</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hornet 4 Drive</td>\n",
       "      <td>6</td>\n",
       "      <td>110</td>\n",
       "      <td>3.215</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Hornet Sportabout</td>\n",
       "      <td>8</td>\n",
       "      <td>175</td>\n",
       "      <td>3.440</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Model  cyl   hp     wt  vs  gear\n",
       "0          Mazda RX4    6  110  2.620   0     4\n",
       "1      Mazda RX4 Wag    6  110  2.875   0     4\n",
       "2         Datsun 710    4   93  2.320   1     4\n",
       "3     Hornet 4 Drive    6  110  3.215   1     3\n",
       "4  Hornet Sportabout    8  175  3.440   0     3"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cars.loc [[0,1,2,3,4], ['Model', 'cyl', 'hp', 'wt', 'vs', 'gear']]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7be70c88-42d7-4c4d-82df-bbeef6884927",
   "metadata": {},
   "source": [
    "#### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e3726955-7535-4858-95f5-66128b5ced4d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Model    Mazda RX4\n",
       "mpg           21.0\n",
       "cyl              6\n",
       "disp         160.0\n",
       "hp             110\n",
       "drat           3.9\n",
       "wt            2.62\n",
       "qsec         16.46\n",
       "vs               0\n",
       "am               1\n",
       "gear             4\n",
       "carb             4\n",
       "Name: 0, dtype: object"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cars.iloc [0]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7fc33e94-dcee-4a3b-b198-d50cb783f0e6",
   "metadata": {},
   "source": [
    "#### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "05100d82-cae1-4359-a286-b91cb34e169e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>cyl</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    cyl\n",
       "23    8"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cars.loc [[23],['cyl']]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "397066c2-aed4-4127-9e43-462631e53c7e",
   "metadata": {},
   "source": [
    "#### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4\n",
    "#### Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "3e078d68-c779-408b-892b-d1a366fb6aa3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>cyl</th>\n",
       "      <th>gear</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>6</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>8</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    cyl  gear\n",
       "1     6     4\n",
       "18    4     4\n",
       "28    8     5"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cars.loc [[1, 18, 28],['cyl', 'gear']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0635688-4e18-43ad-961c-0a0af550508d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
