clearvars; close all; clc;

%% File's directory and the list of file names

path = 'coefzdg/';
%path = 'coefzdgun/';
svpath = '../../zfiles/';

files = dir(path);
files = rmfield(files, 'folder');
files = rmfield(files, 'bytes');
files = rmfield(files, 'datenum');
files = rmfield(files, 'isdir');
files = rmfield(files, 'date');
files(1:2) = [];
files = {files.name}.';

%% Get total energy from every scale
% Energy_tot=
%  square root of 1/N * sigma(i to length of scale) Energy_i

data_energy = zeros(length(files),181);
for i=1:length(files)
    disp(['File name: ' files{i,1}]);
    load([path files{i}]);
    row = size(gaucoef,1);
    wavegy = zeros(1,row);
    for j=1:row
        disp(['--Get total energy at scale: ' num2str(j+19)])
        the_egy = sqrt((1/length(gaucoef{j,1}))*sum(gaucoef{j,1}.^2));
        disp(['----Total energy: ' num2str(the_egy)])
        wavegy(1,j) = the_egy;
    end
    data_energy(i,:)=wavegy(1,:);
end
%save([svpath 'energy_db8.mat'],'data_energy','-v7.3');
save([svpath 'cwt181morl_fea.mat'],'data_energy','-v7.3');
%save([svpath 'cwt181morlunpre_fea.mat'],'data_energy','-v7.3');
%save([svpath 'energy_haar.mat'],'data_energy','-v7.3');