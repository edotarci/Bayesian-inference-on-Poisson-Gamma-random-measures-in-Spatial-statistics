%% LOAD data

data_raw = load('data_fires_selection_SeaWE.mat');
data = data_raw;

%%% select Initial and Final date %%%
% Years 2014-2020  -->  T = 81 months
% pos_ini = find(data.dates >= '01-January-2014', 1);
% pos_fin = find(data.dates >= '01-September-2020', 1);

% % Years 2018-2020  -->  T = 33 months
% pos_ini = find(data.dates >= '01-January-2018', 1);
% pos_fin = find(data.dates >= '01-September-2020', 1);

% % Years 2018  -->  T = 12 months
% pos_ini = find(data.dates >= '01-January-2018', 1);
% pos_fin = find(data.dates >= '01-December-2018', 1);

%% onee single observation

pos_ini = find(data.dates >= initial_date, 1);
pos_fin = find(data.dates >= final_date, 1);

T   = pos_fin - pos_ini + 1;
obs = data.obsA(pos_ini:pos_fin);
Nyt = data.NtA(pos_ini:pos_fin);

data.scale = 10^(-2);
data.T   = T;
data.obs = obs;
data.Nyt = Nyt;   % fprintf(['\n\n%%%%%% Number of observations: %%%%%% \n     Nyt = ',num2str(Nyt),'\n\n'])

% space S - observations, allocations, theta
data.limX   = [data.lon1int_out,data.lon2int_out];
data.limY   = [data.lat1int_out,data.lat2int_out];
% space X - obsevations used for inference
data.limXin = [data.lon1int,data.lon2int];   limXin_theta = data.limXin;
data.limYin = [data.lat1int,data.lat2int];   limYin_theta = data.limYin;



%% Build MASK for coast

% Include sea on the west   --   (lon1int = -67.5;   lon2int = -61.0)
% extW = -10.0;
% data.limX   = [data.lon1int_out+extW, data.lon2int_out];
% data.limXin = [data.lon1int    +extW, data.lon2int];
% sea = 'west';
% data.limYin = [data.lat1int,data.lat2int];


% Include sea on the west + east   --   (lon1int = -67.5;   lon2int = -38.0)
% extW = -10.0;
% extE = + 0.0;
% data.limX   = [data.lon1int_out+extW, data.lon2int_out+extE];
% data.limXin = [data.lon1int+extW,     data.lon2int+extE];
% sea = 'west-east';

% % select subset of the above [long -67.5 to -50.0,   lat -36.5 to -16.0]
% data.limX(2)   = -50.0+2.0;
% data.limXin(2) = -50.0;

% % select only 'square' with  [long -70.0 to -60.0,   lat -40.0 to -20.0]
latmin = 20;
latmax = 30;
longmax = 65;
longmin = 55;
data.limX   = [-longmax-2.0, -longmin+2.0];
data.limXin = [-longmax,     -longmin];
data.limY   = [-latmax-2.0, -latmin+2.0];
data.limYin = [-latmax,     -latmin];

% % select only 'strip' with lat max = -21.0
% data.limYin = [data.lat1int,     -21.0];
% data.limY   = [data.lat1int_out, -21.0+2.0];

% sub-select the observations
for t=1:T
   tmp = data.obs{t};
   test = (tmp(:,1) > data.limXin(1)) & (tmp(:,1) < data.limXin(2)) & ...
          (tmp(:,2) > data.limYin(1)) & (tmp(:,2) < data.limYin(2));
   data.obs{t} = tmp(test,:);
end
