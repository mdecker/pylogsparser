"""
quick & dirty tester for examples included in the definition files

"""
import os

from logsparser import lognormalizer

normalizer_path = os.environ['NORMALIZERS_PATH'] if 'NORMALIZERS_PATH' in os.environ else '../normalizers/'
ln = lognormalizer.LogNormalizer(normalizer_path)

def main():
    for appliedto in ln.normalizers:
        for normalizer in ln.normalizers[appliedto]:
            for patternname in normalizer.patterns:
                pattern = normalizer.patterns[patternname]
                for example in pattern.examples:
                    description = example.get_description()
                    tst_data = { appliedto: description['sample'] }
                    ln.lognormalize(tst_data)
                    for tagname in description['normalization']:
                        if not tagname in tst_data:
                            raise Exception("{pn}/{tn} not found".format(pn=patternname, tn=tagname))
                        else:
                            # convert parsed value to string as expected values are also strings
                            tst_val = str(tst_data[tagname])
                            desc_val = description['normalization'][tagname]
                            if not tst_val == desc_val:
                                raise Exception("{pn}/{tn}: wrong value: '{fv}' vs. '{ev}'".format(pn=patternname, tn=tagname, fv=tst_val, ev=desc_val))
            
if __name__ == "__main__":
    main()
