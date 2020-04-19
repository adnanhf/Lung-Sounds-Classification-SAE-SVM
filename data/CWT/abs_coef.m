clearvars; close all; clc;

%% File's directory and the list of file names

path = 'coefzdr/';
%path = 'coefzdrun/';
svpath = 'coefzda/';
%svpath = 'coefzdaun/';

files = dir(path);
files = rmfield(files, 'folder');
files = rmfield(files, 'bytes');
files = rmfield(files, 'datenum');
files = rmfield(files, 'isdir');
files = rmfield(files, 'date');
files(1:2) = [];
files = {files.name}.';

%% Process coefficients with non-linearity

for i=1:length(files)
    disp(['File name: ' files{i,1}])
    load([path files{i}]);
    [row,col] = size(rawcoef);
    abscoef = zeros(row,col);
    for j=1:row
        %disp(['--Compute non-linearity at scale: ' num2str(j+19)])
        the_abs = abs(rawcoef(j,:));
        abscoef(j,:) = the_abs;
    end
    save([svpath files{i}],'abscoef','-v7');
end
