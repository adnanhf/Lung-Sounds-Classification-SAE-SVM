clearvars; close all; clc;

%% File's directory and the list of file names

path = 'coefzda/';
%path = 'coefzdaun/';
svpath = 'coefzdg/';
%svpath = 'coefzdgun/';

files = dir(path);
files = rmfield(files, 'folder');
files = rmfield(files, 'bytes');
files = rmfield(files, 'datenum');
files = rmfield(files, 'isdir');
files = rmfield(files, 'date');
files(1:2) = [];
files = {files.name}.';

%% Smooth coefficients after processed by non-linearity

for i=1:length(files)
    disp(['File name: ' files{i,1}])
    load([path files{i}]);
    row = size(abscoef,1);
    gaucoef = cell(row,1);
    for j=1:row
        %disp(['--Smoothing at scale: ' num2str(j+19)])
        gauwn = gausswin(j+19,1);
        the_gau = conv(abscoef(j,:),gauwn);
        gaucoef{j} = the_gau;
    end
    save([svpath files{i}],'gaucoef','-v7');
end
