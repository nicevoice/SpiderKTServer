
import DailyFxSpiderUtils


if __name__ =='__main__':
    
    startContext = DailyFxSpiderUtils.retrunStartContext('http://cdn.dailyfx.com.hk/livenews/index.html')
    print DailyFxSpiderUtils.divisionTarget(startContext,'<tr class="record" valign="top">', '</tr>')
    print len(DailyFxSpiderUtils.findAllTarget(startContext))








