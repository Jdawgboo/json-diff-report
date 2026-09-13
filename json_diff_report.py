import argparse,json

def diff(before,after,path=''):
 out=[]
 for key in sorted(set(before)|set(after)):
  here=f'{path}.{key}' if path else key
  if key not in before: out.append({'path':here,'change':'added'})
  elif key not in after: out.append({'path':here,'change':'removed'})
  elif isinstance(before[key],dict) and isinstance(after[key],dict): out+=diff(before[key],after[key],here)
  elif before[key]!=after[key]: out.append({'path':here,'change':'changed','before':before[key],'after':after[key]})
 return out

def main():
 p=argparse.ArgumentParser(); p.add_argument('before');p.add_argument('after');a=p.parse_args()
 with open(a.before) as f: left=json.load(f)
 with open(a.after) as f: right=json.load(f)
 print(json.dumps(diff(left,right),indent=2,sort_keys=True))
if __name__=='__main__': main()
