#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture()
def generate_data():
    data = \
        {
            'devices': [
                {
                    'status': 3,
                    'product': 'R9PlusmA',
                    'browser': {
                        'selected': True,
                        'apps': [
                            {
                                'name': 'Browser',
                                'developer': 'GoogleInc.',
                                'selected': True,
                                'type': 'android-browser',
                                'system': True,
                                'id': 'com.android.browser/.RealBrowserActivity'
                            }
                        ]
                    },
                    'reverseForwards': [

                    ],
                    'battery': {
                        'status': 'full',
                        'source': 'usb',
                        'scale': 100,
                        'health': 'good',
                        'voltage': 4.262,
                        'temp': 29.7,
                        'level': 100
                    },
                    'statusChangedAt': '2016-10-21T13: 29: 16.111Z',
                    'operator': ',',
                    'owner': None,
                    'airplaneMode': False,

                    'presenceChangedAt': '2016-10-22T03: 28: 40.586Z',
                    'ready': True,
                    'using': False,
                    'serial': '778d4f10',
                    'createdAt': '2016-10-21T12: 30: 24.250Z',
                    'sdk': '22',
                    'network': {
                        'subtype': '',
                        'failover': False,
                        'connected': True,
                        'roaming': False,
                        'type': 'WIFI'
                    },
                    'remoteConnect': False,
                    'abi': 'arm64-v8a',
                    'remoteConnectUrl': None,
                    'platform': 'Android',
                    'version': '5.1.1',
                    'present': False,
                    'provider': {
                        'name': 'red-Inspiron-3647',
                        'channel': 'O1HNR2n6Q+iWYV2YAEZRhw=='
                    },
                    'model': 'R9PlusmA',
                    'manufacturer': 'OPPO',
                    'display': {
                        'secure': True,
                        'density': 3,
                        'url': 'ws: //10.12.147.98: 7424',
                        'height': 1920,
                        'xdpi': 370.7019958496094,
                        'width': 1080,
                        'fps': 60,
                        'rotation': 0,
                        'id': 0,
                        'ydpi': 369.4540100097656,
                        'size': 5.957783222198486
                    },
                    'channel': 'a/nbaUCQMduULvq/8HeNTwtCWNs=',
                    'phone': {
                        'imei': '862732035986079',
                        'iccid': None,
                        'phoneNumber': None,
                        'network': 'UNKNOWN'
                    }
                },
                {
                    'status': 3,
                    'product': 'N5117',
                    'browser': {
                        'selected': False,
                        'apps': [
                            {
                                'name': 'Browser',
                                'developer': 'GoogleInc.',
                                'selected': False,
                                'type': 'android-browser',
                                'system': True,
                                'id': 'com.android.browser/.RealBrowserActivity'
                            }
                        ]
                    },
                    'reverseForwards': [

                    ],
                    'statusChangedAt': '2016-12-15T03: 14: 22.417Z',
                    'operator': None,
                    'owner': None,
                    'airplaneMode': False,
                    'presenceChangedAt': '2016-12-21T03: 56: 37.509Z',
                    'ready': True,
                    'using': False,
                    'serial': '9be75a9b',
                    'createdAt': '2016-10-22T03: 31: 17.129Z',
                    'manufacturer': 'OPPO',
                    'network': {
                        'subtype': '',
                        'failover': False,
                        'connected': True,
                        'roaming': False,
                        'type': 'WIFI'
                    },
                    'remoteConnect': False,
                    'abi': 'armeabi-v7a',
                    'remoteConnectUrl': None,
                    'platform': 'Android',
                    'version': '4.3',
                    'present': False,
                    'provider': {
                        'name': 'red-Inspiron-3647',
                        'channel': 'DSvnAQnqRUe6/ROim+ogjQ=='
                    },
                    'model': 'N5117',
                    'sdk': '18',
                    'display': {
                        'secure': True,
                        'density': 2,
                        'url': 'ws: //10.12.144.16: 7516',
                        'height': 1280,
                        'xdpi': 309.96600341796875,
                        'width': 720,
                        'fps': 61,
                        'rotation': 0,
                        'id': 0,
                        'ydpi': 312.614990234375,
                        'size': 4.7074875831604
                    },
                    'channel': '8d6J8hsyZkqKz3ncKSkyzTWskM4=',
                    'phone': {
                        'imei': '864181023864435',
                        'iccid': None,
                        'phoneNumber': None,
                        'network': 'UNKNOWN'
                    }
                },
                {
                    'status': 1,
                    'product': 'kltezn',
                    'browser': {
                        'selected': False,
                        'apps': [
                            {
                                'name': 'Browser',
                                'developer': 'Samsung',
                                'selected': False,
                                'type': 'samsung-sbrowser',
                                'system': True,
                                'id': 'com.sec.android.app.sbrowser/.SBrowserLauncherActivity'
                            }
                        ]
                    },
                    'reverseForwards': [

                    ],
                    'battery': {
                        'status': 'charging',
                        'source': 'usb',
                        'scale': 100,
                        'health': 'good',
                        'voltage': 4.32,
                        'temp': 30.4,
                        'level': 100
                    },
                    'statusChangedAt': '2016-12-19T08: 10: 28.022Z',
                    'operator': None,
                    'owner': None,
                    'airplaneMode': False,
                    'presenceChangedAt': '2016-12-19T08: 10: 28.055Z',
                    'ready': False,
                    'using': False,
                    'serial': 'fe3eb2b6',
                    'createdAt': '2016-10-21T12: 42: 30.030Z',
                    'sdk': '23',
                    'network': {
                        'subtype': '',
                        'failover': False,
                        'connected': True,
                        'roaming': False,
                        'type': 'WIFI'
                    },
                    'remoteConnect': False,
                    'abi': 'armeabi-v7a',
                    'remoteConnectUrl': None,
                    'platform': 'Android',
                    'version': '6.0.1',
                    'present': False,
                    'provider': {
                        'name': 'red-Inspiron-3647',
                        'channel': 'DSvnAQnqRUe6/ROim+ogjQ=='
                    },
                    'model': 'SM-G9006V',
                    'manufacturer': 'SAMSUNG',
                    'display': {
                        'secure': True,
                        'density': 3,
                        'url': 'ws: //10.12.144.16: 7424',
                        'height': 1920,
                        'xdpi': 422.0299987792969,
                        'width': 1080,
                        'fps': 60,
                        'rotation': 0,
                        'id': 0,
                        'ydpi': 424.0690002441406,
                        'size': 5.200733661651611
                    },
                    'channel': '9ZhYZvGxjWkUaX2UmKDCRqKZmp0=',
                    'phone': {
                        'imei': '352621066378644',
                        'iccid': None,
                        'phoneNumber': None,
                        'network': 'UNKNOWN'
                    }
                },
                {
                    'status': 3,
                    'product': 'h3gduoszn',
                    'browser': {
                        'selected': True,
                        'apps': [
                            {
                                'name': 'Browser',
                                'developer': 'Samsung',
                                'selected': True,
                                'type': 'samsung-sbrowser',
                                'system': True,
                                'id': 'com.sec.android.app.sbrowser/.SBrowserMainActivity'
                            }
                        ]
                    },
                    'reverseForwards': [

                    ],
                    'battery': {
                        'status': 'full',
                        'source': 'usb',
                        'scale': 100,
                        'health': 'good',
                        'voltage': 4.327,
                        'temp': 32.1,
                        'level': 100
                    },
                    'statusChangedAt': '2016-12-19T07: 11: 23.626Z',
                    'operator': ',',
                    'owner': None,
                    'airplaneMode': False,
                    'presenceChangedAt': '2016-12-19T07: 11: 23.423Z',
                    'ready': True,
                    'using': False,
                    'serial': 'e1a0ee1a',
                    'createdAt': '2016-12-01T08: 36: 39.627Z',
                    'sdk': '21',
                    'network': {
                        'subtype': None,
                        'failover': False,
                        'connected': False,
                        'roaming': False,
                        'type': None
                    },
                    'remoteConnect': False,
                    'abi': 'armeabi-v7a',
                    'remoteConnectUrl': None,
                    'platform': 'Android',
                    'version': '5.0',
                    'present': True,
                    'provider': {
                        'name': 'red-Inspiron-3647',
                        'channel': 'DSvnAQnqRUe6/ROim+ogjQ=='
                    },
                    'model': 'SM-N9002',
                    'manufacturer': 'SAMSUNG',
                    'display': {
                        'secure': True,
                        'density': 3,
                        'url': 'ws: //10.12.144.16: 7664',
                        'height': 1920,
                        'xdpi': 386.3659973144531,
                        'width': 1080,
                        'fps': 60,
                        'rotation': 0,
                        'id': 0,
                        'ydpi': 387.0469970703125,
                        'size': 5.69398832321167
                    },
                    'channel': 'uAvfZRB+OfHpOoFZikYconvRw+I=',
                    'phone': {
                        'imei': '354224061720841',
                        'iccid': None,
                        'phoneNumber': None,
                        'network': 'UNKNOWN'
                    }
                },
                {
                    'status': 3,
                    'product': 'L39h',
                    'browser': {
                        'selected': False,
                        'apps': [

                        ]
                    },
                    'reverseForwards': [

                    ],
                    'battery': {
                        'status': 'full',
                        'source': 'usb',
                        'scale': 100,
                        'health': 'good',
                        'voltage': 4.287,
                        'temp': 29.1,
                        'level': 100
                    },
                    'statusChangedAt': '2016-12-15T03: 14: 31.020Z',
                    'operator': u'\u4e2d\u56fd\u8054\u901a',
                    'owner': None,
                    'airplaneMode': False,
                    'presenceChangedAt': '2016-12-19T07: 05: 44.377Z',
                    'ready': True,
                    'using': False,
                    'serial': 'BH90168J1J',
                    'createdAt': '2016-10-28T11: 52: 13.474Z',
                    'sdk': '19',
                    'network': {
                        'failover': False,
                        'manual': False,
                        'subtype': '',
                        'state': 'in_service',
                        'connected': True,
                        'operator': u'\u4e2d\u56fd\u8054\u901a',
                        'roaming': False,
                        'type': 'WIFI'
                    },
                    'remoteConnect': False,
                    'abi': 'armeabi-v7a',
                    'remoteConnectUrl': None,
                    'platform': 'Android',
                    'version': '4.4.2',
                    'present': False,
                    'provider': {
                        'name': 'red-Inspiron-3647',
                        'channel': 'DSvnAQnqRUe6/ROim+ogjQ=='
                    },
                    'model': 'L39h',
                    'manufacturer': 'SONY',
                    'display': {
                        'secure': True,
                        'density': 3,
                        'url': 'ws: //10.12.144.16: 7684',
                        'height': 1920,
                        'xdpi': 442.45098876953125,
                        'width': 1080,
                        'fps': 60,
                        'rotation': 0,
                        'id': 0,
                        'ydpi': 443.3450012207031,
                        'size': 4.971247673034668
                    },
                    'channel': 'ssK2BDmX4Pm6cWRxMTVPqGplC8s=',
                    'phone': {
                        'imei': '358094058424194',
                        'iccid': '89860115831012343258',
                        'phoneNumber': '+8618521771476',
                        'network': 'HSPA'
                    }
                },
                {
                    'status': 3,
                    'product': 'm7cdug',
                    'browser': {
                        'selected': False,
                        'apps': [
                            {
                                'name': 'Browser',
                                'developer': 'GoogleInc.',
                                'selected': False,
                                'type': 'android-browser',
                                'system': True,
                                'id': 'com.android.browser/.BrowserActivity'
                            },
                            {
                                'name': 'Chrome',
                                'developer': 'GoogleInc.',
                                'selected': False,
                                'type': 'chrome',
                                'system': True,
                                'id': 'com.android.chrome/com.google.android.apps.chrome.Main'
                            }
                        ]
                    },
                    'reverseForwards': [

                    ],
                    'battery': {
                        'status': 'charging',
                        'source': 'usb',
                        'scale': 100,
                        'health': 'good',
                        'voltage': 3.733,
                        'temp': 36.4,
                        'level': 35
                    },
                    'statusChangedAt': '2016-10-28T12: 08: 56.434Z',
                    'operator': None,
                    'owner': None,
                    'airplaneMode': False,
                    'presenceChangedAt': '2016-10-28T12: 10: 29.571Z',
                    'ready': True,
                    'using': False,
                    'serial': 'HC34WW905103',
                    'createdAt': '2016-10-28T12: 06: 00.758Z',
                    'sdk': '17',
                    'network': {
                        'subtype': '',
                        'failover': False,
                        'connected': True,
                        'roaming': False,
                        'type': 'WIFI'
                    },
                    'remoteConnect': False,
                    'abi': 'armeabi-v7a',
                    'remoteConnectUrl': None,
                    'platform': 'Android',
                    'version': '4.2.2',
                    'present': False,
                    'provider': {
                        'name': 'red-Inspiron-3647',
                        'channel': '6VQ54XWTRsOI0H1tEPxOyg=='
                    },
                    'model': '802w',
                    'manufacturer': 'HTC',
                    'display': {
                        'secure': True,
                        'density': 3,
                        'url': 'ws: //10.12.144.16: 7584',
                        'height': 1920,
                        'xdpi': 472.9649963378906,
                        'width': 1080,
                        'fps': 60,
                        'rotation': 0,
                        'id': 0,
                        'ydpi': 473.4750061035156,
                        'size': 4.653842926025391
                    },
                    'channel': 'JUa9vSz2k34yeD8ooSyg5N8hU3g=',
                    'phone': {
                        'imei': '355868050315606',
                        'iccid': '89860114831009528060',
                        'phoneNumber': '+8614530607556',
                        'network': 'UNKNOWN'
                    }
                },
                {
                    'status': 3,
                    'product': 'R7',
                    'browser': {
                        'selected': True,
                        'apps': [
                            {
                                'name': 'Browser',
                                'developer': 'GoogleInc.',
                                'selected': True,
                                'type': 'android-browser',
                                'system': True,
                                'id': 'com.android.browser/.RealBrowserActivity'
                            }
                        ]
                    },
                    'reverseForwards': [

                    ],
                    'battery': {
                        'status': 'charging',
                        'source': 'usb',
                        'scale': 100,
                        'health': 'good',
                        'voltage': 4.165,
                        'temp': 29,
                        'level': 83
                    },
                    'statusChangedAt': '2016-12-26T01: 59: 41.431Z',
                    'operator': None,
                    'owner': None,
                    'airplaneMode': False,
                    'presenceChangedAt': '2016-12-26T01: 59: 41.992Z',
                    'ready': True,
                    'using': False,
                    'serial': 'MRO7VW6STGKZJNKZ',
                    'createdAt': '2016-11-28T10: 51: 32.099Z',
                    'sdk': '19',
                    'network': {
                        'subtype': '',
                        'failover': False,
                        'connected': True,
                        'roaming': False,
                        'type': 'WIFI'
                    },
                    'remoteConnect': False,
                    'abi': 'armeabi-v7a',
                    'remoteConnectUrl': None,
                    'platform': 'Android',
                    'version': '4.4.4',
                    'present': True,
                    'provider': {
                        'name': 'red-Inspiron-3647',
                        'channel': 'DSvnAQnqRUe6/ROim+ogjQ=='
                    },
                    'model': 'R7',
                    'manufacturer': 'OPPO',
                    'display': {
                        'secure': True,
                        'density': 3,
                        'url': 'ws: //10.12.144.16: 7596',
                        'height': 1920,
                        'xdpi': 442.45098876953125,
                        'width': 1080,
                        'fps': 59.06999969482422,
                        'rotation': 0,
                        'id': 0,
                        'ydpi': 439.35101318359375,
                        'size': 5.005581378936768
                    },
                    'channel': '4CnBXaOMdwgkYblOxCzsswrxHZ0=',
                    'phone': {
                        'imei': '868064022230822',
                        'iccid': None,
                        'phoneNumber': None,
                        'network': 'UNKNOWN'
                    }
                },
                {
                    'status': 3,
                    'product': 'M3s',
                    'browser': {
                        'selected': True,
                        'apps': [
                            {
                                'name': 'Browser',
                                'developer': 'GoogleInc.',
                                'selected': True,
                                'type': 'android-browser',
                                'system': True,
                                'id': 'com.android.browser/.BrowserActivity'
                            }
                        ]
                    },
                    'reverseForwards': [

                    ],
                    'battery': {
                        'status': 'full',
                        'source': 'usb',
                        'scale': 100,
                        'health': 'good',
                        'voltage': 4.417,
                        'temp': 34,
                        'level': 100
                    },
                    'statusChangedAt': '2016-12-07T09: 03: 30.854Z',
                    'operator': ',',
                    'owner': None,
                    'airplaneMode': False,
                    'presenceChangedAt': '2016-12-12T07: 35: 49.792Z',
                    'ready': True,
                    'using': False,
                    'serial': 'Y15QKBP323GGV',
                    'createdAt': '2016-12-07T09: 02: 41.845Z',
                    'sdk': '22',
                    'network': {
                        'subtype': '',
                        'failover': False,
                        'connected': True,
                        'roaming': False,
                        'type': 'WIFI'
                    },
                    'remoteConnect': False,
                    'abi': 'arm64-v8a',
                    'remoteConnectUrl': None,
                    'platform': 'Android',
                    'version': '5.1',
                    'present': False,
                    'provider': {
                        'name': 'red-Inspiron-3647',
                        'channel': 'pSi60xnaQP6anibXbtJvyw=='
                    },
                    'model': 'M3s',
                    'manufacturer': 'MEIZU',
                    'display': {
                        'secure': True,
                        'density': 2,
                        'url': 'ws: //10.12.144.16: 7452',
                        'height': 1280,
                        'xdpi': 320,
                        'width': 720,
                        'fps': 57.99000549316406,
                        'rotation': 0,
                        'id': 0,
                        'ydpi': 320,
                        'size': 4.589389801025391
                    },
                    'channel': 'x7RKS3VuDTxP/qHCqVAJYNBBJAg=',
                    'phone': {
                        'imei': '86229903536379',
                        'iccid': None,
                        'phoneNumber': None,
                        'network': 'UNKNOWN'
                    }
                },
                {
                    'status': 2,
                    'ready': False,
                    'reverseForwards': [

                    ],
                    'statusChangedAt': '2016-11-18T05: 55: 02.443Z',
                    'remoteConnectUrl': None,
                    'remoteConnect': False,
                    'presenceChangedAt': '2016-11-18T12: 03: 26.915Z',
                    'createdAt': '2016-11-18T05: 55: 01.519Z',
                    'provider': {
                        'name': 'red-Inspiron-3647',
                        'channel': '0e8BxImgQ9Wm38GOl6s7Pw=='
                    },
                    'owner': None,
                    'using': False,
                    'serial': 'd33cc1c4',
                    'present': False
                }
            ],
            'success': True
        }
    return data
